import yaml
import json

import pandas as pd
import numpy as np
import tensorflow as tf

from pathlib import Path
from pymatgen.core import Structure
from sklearn.model_selection import train_test_split
from megnet.models import MEGNetModel
from megnet.data.crystal import CrystalGraph




def read_pymatgen_dict(file):
    with open(file, "r") as f:
        d = json.load(f)
    return Structure.from_dict(d)


def energy_within_threshold(prediction, target):
    # compute absolute error on energy per system.
    # then count the no. of systems where max energy error is < 0.02.
    e_thresh = 0.02
    error_energy = tf.math.abs(target - prediction)

    success = tf.math.count_nonzero(error_energy < e_thresh)
    total = tf.size(target)
    return success / tf.cast(total, tf.int64)

def prepare_dataset(dataset_path):
    dataset_path = Path(dataset_path)
    targets = pd.read_csv(dataset_path / "targets.csv", index_col=0)
    struct = {
        item.name.strip(".json"): read_pymatgen_dict(item)
        for item in (dataset_path / "structures").iterdir()
    }

    data = pd.DataFrame(columns=["structures"], index=struct.keys())
    data = data.assign(structures=struct.values(), targets=targets)

    return train_test_split(data, test_size=0.25, random_state=666)

 
def prepare_model(cutoff, lr):
    nfeat_bond = 10
    r_cutoff = cutoff
    gaussian_centers = np.linspace(0, r_cutoff + 1, nfeat_bond)
    gaussian_width = 0.8
    
    return MEGNetModel(
        graph_converter=CrystalGraph(cutoff=r_cutoff),
        centers=gaussian_centers,
        width=gaussian_width,
        loss=["MAE"],
        npass=2,
        lr=lr,
        metrics=energy_within_threshold
    )


def main(config):
    train, test = prepare_dataset(config["datapath"])
    model = prepare_model(
        float(config["model"]["cutoff"]),
        float(config["model"]["lr"]), 
    )
    model.train(
        train.structures,
        train.targets,
        validation_structures=test.structures,
        validation_targets=test.targets,
        epochs=int(config["model"]["epochs"]),
        batch_size=int(config["model"]["batch_size"]),
    )


if __name__ == "__main__":
    with open("config.yaml") as file:
        config = yaml.safe_load(file)
    main(config)

import yaml
import pandas as pd

from pathlib import Path
from baseline import prepare_model
from baseline import read_pymatgen_dict



def main(config):
    model = prepare_model(
        float(config["model"]["cutoff"]), float(config["model"]["lr"])
    )
    model.load_weights(config['checkpoint_path'])

    dataset_path = Path(config['test_datapath'])
    struct = {item.name.strip('.json'): read_pymatgen_dict(item) for item in (dataset_path/'structures').iterdir()}
    private_test = pd.DataFrame(columns=['id', 'structures'], index=struct.keys())
    private_test = private_test.assign(structures=struct.values())
    private_test = private_test.assign(predictions=model.predict_structures(private_test.structures))
    private_test[['predictions']].to_csv('./submission.csv', index_label='id')

if __name__ == '__main__':
    with open("config.yaml") as file:
        config = yaml.safe_load(file)
    main(config)
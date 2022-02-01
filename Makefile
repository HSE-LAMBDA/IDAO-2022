all: build

build:
	@echo 'starting....'
	bash train.sh
	bash run.sh
run:
	bash run.sh
train:
	bash train.sh
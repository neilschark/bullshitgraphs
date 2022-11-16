# bullshitgraphs

While researching for my masters thesis I found many papers which included graphs which had a questionable value, besides including as many buzzwords as possible.

This gave me the idea, that the graphs for this kind of papers can be automated.

This project uses poetry.

```
poetry install
poetry shell
python bullshitgraphs.py importantkeyword1 importantkeyword2 andsoon andsoforth
```


## Build docker image

```
docker build -t ghcr.io/neilschark/bullshitgraphs:latest .
```
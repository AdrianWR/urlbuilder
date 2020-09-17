# AIvsCOVID19  URL Builder

## Motivation
This repository contains a simple setup to create a URL Builder instance to act in the context of Data Mining workflow in the AIvsCOVID19 project. The URL Builder is a special type of data mining Python script; it iterates through search pages from a scientific article website, gathering all the links which could have valuable data to extract in a further process. At each iteration, the URL Builder will send the links extracted to a Google BigQuery table, given the right permissions to write data.

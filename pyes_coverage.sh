#!/bin/sh

PYTHONPATH= nosetests3 --with-coverage3 --cover3-html --cover3-html-dir=`pwd`/pyes_coverage --cover3-branch --cover3-erase --all

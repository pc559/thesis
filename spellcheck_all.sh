#!/bin/bash
for f in *_chapter.tex; do aspell -c -t $f; done
aspell -c -t thesis.tex

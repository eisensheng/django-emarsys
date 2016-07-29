#!/usr/bin/env sh

# install pip-tools' future branch that has pip-compile
if ! command -v pip-compile >/dev/null 2>&1; then
    pip install --upgrade pip
    pip install git+https://github.com/nvie/pip-tools.git@future
fi

for name in runtime testing; do
    pip-compile --annotate \
        --output-file "requirements/requirements-${name}.txt" \
        "requirements/in/requirements-${name}.in"
done

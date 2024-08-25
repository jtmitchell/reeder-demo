set dotenv-load := true

# This list of available targets
default:
    @just --list

# Run the tests
test:
    uv run pytest

# Build the package
build:
    uvx --from build pyproject-build --installer uv

# Make virtual environment
venv:
    uv venv --python python3.12

# Install python DEV dependancies
install:
    uv sync
    uv run pre-commit install --hook-type pre-commit --hook-type commit-msg

# Run the bump2version command
bumpversion +options="build":
    uv run bump2version {{options}}

# Start new develpment cycle with new patch and release candidate
patch_version +options="":
    uv run bump2version patch {{options}} --commit
    git push

# Bump the version for a release. Make tag and commit
release_version:
    uv run bump2version release --tag --commit
    git push && git push --tags

# Show the package version
version:
    @uvx hatch version

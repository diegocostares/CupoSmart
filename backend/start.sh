#!/bin/bash

# Function to check if a file exists
file_exists() {
  if [ -f "$1" ]; then
    return 0
  else
    return 1
  fi
}

# Define the target file path
target_file="data/courses_quota.csv"

# Check if the target file exists
if file_exists "$target_file"; then
  echo "File '$target_file' already exists."
else
  echo "File '$target_file' doesn't exist. Download it first"
  exit 1
fi

# Install dependencies using Poetry
echo "Installing dependencies using Poetry..."
poetry install

# Activate the Poetry shell
echo "Activating Poetry shell..."
poetry shell

# Run uvicorn
echo "Running uvicorn..."
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --reload

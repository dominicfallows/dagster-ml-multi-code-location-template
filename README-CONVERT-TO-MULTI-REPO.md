# Converting to a Multi-Repo Dagster Project

This template is designed for a mono-repo setup, but you can easily split each code location into its own repository for larger teams or stricter isolation.

## Steps to Convert to Multi-Repo

1. **Create a New Repo for Each Code Location**
   - For each code location (e.g., `1_etl-code-location`), create a new GitHub repository (e.g., `my-etl-repo`).
   - Move the code location folder contents into the new repo root.

2. **Update Python Packaging**
   - Ensure each repo has its own `pyproject.toml`, `setup.py`, and `requirements.txt`.
   - Set the package name and version appropriately in each repo.

3. **Adjust Dagster Workspace Configs**
   - In your deployment repo (or orchestrator repo), update `workspace.yaml` and `dagster_cloud.yaml` to reference the remote package or Docker image for each code location.
   - Example for `workspace.yaml`:

     ```yaml
     load_from:
       - python_package:
           package_name: my_etl
           location_name: etl
           executable_path: /path/to/remote/venv/bin/python
     ```

   - Or for Docker:

     ```yaml
     load_from:
       - python_package:
           package_name: my_etl
           location_name: etl
           image: myorg/my-etl:latest
     ```

4. **CI/CD for Each Repo**
   - Set up CI/CD in each code location repo to build and publish the package or Docker image.
   - Optionally, use GitHub Actions to automate deployment to Dagster Cloud or your orchestrator repo.

5. **Shared Code**
   - If you have shared utilities, create a separate `shared_code_location` repo and add it as a dependency in each code location's `requirements.txt`.

## References

- [Dagster Multi-Repo Docs](https://docs.dagster.io/concepts/code-locations#multi-repo-workspaces)
- [Dagster Code Locations](https://docs.dagster.io/deployment/code-locations)
- [workspace.yaml reference](https://docs.dagster.io/deployment/code-locations/workspace-yaml)

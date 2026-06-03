# kube-dash

A simple Django-based Kubernetes dashboard that lists pods from a connected Kubernetes cluster.

## Overview

This project uses Django to render a web page showing pod names, namespaces, and status for all namespaces in the current Kubernetes context.

## Features

- Load Kubernetes configuration from the local machine
- Query the cluster for pods across all namespaces
- Display pod name, namespace, and status in a clean dashboard page

## Requirements

- Python 3.11 or later
- A valid Kubernetes configuration file (`~/.kube/config`) or a working cluster access setup
- The dependencies listed in `requirements.txt`

## Setup

1. Open a terminal in the project root folder.
2. Create a Python virtual environment:

```powershell
python -m venv .venv
```

3. Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Install dependencies:

```powershell
pip install -r requirements.txt
```

5. Run Django migrations:

```powershell
python manage.py migrate
```

## Running the dashboard

1. Make sure your Kubernetes config is available and valid. For example, verify access with:

```powershell
kubectl config view
kubectl get pods --all-namespaces
```

2. Start the Django development server:

```powershell
python manage.py runserver
```

3. Open the dashboard in your browser:

```text
http://127.0.0.1:8000/
```

## Usage

- The home page displays a table of Kubernetes pods.
- It uses the `dashboard.views.home` view, which loads kube config and queries the cluster using `kubernetes.client.CoreV1Api`.
- If the app cannot connect to the cluster, it will render an empty pod list and print the error to the console.

## Admin interface

The Django admin site is available at:

```text
http://127.0.0.1:8000/admin/
```

You can create a superuser if needed:

```powershell
python manage.py createsuperuser
```

## Troubleshooting

- If no pods appear, verify that your Kubernetes context is set correctly.
- If `config.load_kube_config()` fails, confirm your kubeconfig file is present and readable.
- Run the server again after fixing cluster access.

## Project files

- `dashboard/views.py`: fetches pods from Kubernetes and renders the dashboard.
- `dashboard/templates/dashboard/home.html`: dashboard layout and styling.
- `kubeproject/urls.py`: routes the root URL to the dashboard app.
- `dashboard/urls.py`: defines the home page URL.

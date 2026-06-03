from django.shortcuts import render
from kubernetes import client, config

def home(request):

    try:
        # Load kube config
        config.load_kube_config()

        v1 = client.CoreV1Api()

        # Get pods
        pods = v1.list_pod_for_all_namespaces(watch=False)

        pod_list = []

        for pod in pods.items:
            pod_list.append({
                'name': pod.metadata.name,
                'namespace': pod.metadata.namespace,
                'status': pod.status.phase
            })

    except Exception as e:
        pod_list = []
        print(e)

    return render(request, 'dashboard/home.html', {
        'pods': pod_list
    })

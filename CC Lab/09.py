#-Use Python and docker-py or subprocess module to deploy multiple
#container instances and demonstrate scalability

import docker
import time

IMAGE_NAME = "nginx:alpine"      # Lightweight web server image
BASE_NAME = "scalable-nginx"     # Base name for containers


# ---------- CONNECT TO DOCKER ----------
def get_docker_client():
    client = docker.from_env()
    try:
        client.ping()
        print("✅ Connected to Docker daemon.")
    except Exception as e:
        print("❌ Failed to connect to Docker daemon:", e)
        exit(1)
    return client


# ---------- SCALE UP: START MULTIPLE CONTAINERS ----------
def scale_up(client, count):
    containers = []
    print(f"\n📦 Scaling UP: Starting {count} containers...")
    for i in range(1, count + 1):
        name = f"{BASE_NAME}-{i}"
        print(f" → Starting container: {name}")
        container = client.containers.run(
            IMAGE_NAME,
            name=name,
            detach=True,
            ports={"80/tcp": None},  # host pe random port map karega
        )
        containers.append(container)
        time.sleep(0.5)
    return containers


# ---------- SHOW RUNNING CONTAINERS INFO ----------
def show_containers_info(containers):
    print("\n📊 Running container instances:")
    for c in containers:
        c.reload()  # latest info
        ports = c.attrs["NetworkSettings"]["Ports"]["80/tcp"]
        host_port = ports[0]["HostPort"] if ports else "N/A"
        print(f"- {c.name} | ID: {c.short_id} | Status: {c.status} | Host port: {host_port}")


# ---------- SCALE DOWN: STOP + REMOVE ----------
def scale_down(containers):
    print("\n🧹 Scaling DOWN: Stopping and removing containers...")
    for c in containers:
        print(f" → Removing {c.name}")
        try:
            c.stop()
        except Exception:
            pass
        c.remove()
    print("✅ Cleanup done.")


if __name__ == "__main__":
    client = get_docker_client()

    # STEP 1: Pull image (just to be sure)
    print(f"\n⬇️ Pulling image: {IMAGE_NAME} (if not already present)...")
    client.images.pull(IMAGE_NAME)

    # STEP 2: Scale up
    containers = scale_up(client, count=3)

    # STEP 3: Show info (simulate monitoring)
    show_containers_info(containers)

    print("\n⏳ Containers running for a while to simulate workload...")
    time.sleep(10)

    # STEP 4: Scale down
    scale_down(containers)





'''

Pehle requirements

Docker installed hona chahiye (Docker Desktop / Engine)

Python package (agar docker SDK use karna hai):

pip install docker

🟢 Approach 1: docker-py (Docker SDK for Python)

Ye script:

ek Docker image choose karega (e.g. nginx:alpine)

multiple containers start karega (scale up)

unka status print karega

phir sabko stop + remove karega (cleanup)


'''
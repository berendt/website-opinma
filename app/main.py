from flask import Flask, render_template, url_for, g
import yaml

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ceph/")
def ceph():
    return render_template("ceph.html")

@app.route("/openstack/")
def openstack():
    openstack_data = get_openstack_data()
    return render_template("openstack.html", tabs=openstack_data["tabs"])

@app.route("/openstack/<service>/")
def openstack_service(service):
    openstack_data = get_openstack_data()
    return render_template("openstack_service.html", tabs=openstack_data["tabs"], service=service)

@app.route("/kubernetes/")
def kubernetes():
    return render_template("kubernetes.html")

@app.route("/stuttgart/")
def stuttgart():
    return render_template("stuttgart.html")

def get_openstack_data():
    if 'openstack_data' not in g:
        with open("data/openstack_components.yaml") as fp:
            g.openstack_data = yaml.load(fp)

    return g.openstack_data

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

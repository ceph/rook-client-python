from os.path import expanduser

import yaml
import pytest

from rook_ceph_client.cephcluster import CephCluster
from rook_ceph_client.cephfilesystem import CephFilesystem
from rook_ceph_client.cephnfs import CephNFS
from rook_ceph_client.cephobjectstore import CephObjectStore


def load_example(what):
    import requests

    url = f'https://raw.githubusercontent.com/rook/rook/master/cluster/examples/kubernetes/ceph/{what}.yaml'
    r = requests.get(url, allow_redirects=True)
    return yaml.safe_load(r.content.decode('utf-8'))

    #with open(expanduser('~/go/src/github.com/rook/rook/cluster/examples/kubernetes/ceph/{what}.yaml').format(what=what)) as f:
    #    return yaml.safe_load(f.read())

@pytest.mark.parametrize(
    "filename",
    [
        "cluster-external",
        "cluster-minimal",
        "cluster-on-pvc",
        "cluster-test",
        "cluster",
    ],
)
def test_cluster(filename):
    crd = load_example(filename)
    c = CephCluster.from_json(crd)
    assert crd == c.to_json()


@pytest.mark.parametrize(
    "filename",
    [
        "filesystem-ec",
        "filesystem-test",
        "filesystem",
    ],
)
def test_filesystem(filename):
    crd = load_example(filename)
    c = CephFilesystem.from_json(crd)
    assert crd == c.to_json()

@pytest.mark.parametrize(
    "filename",
    [
        "object-bucket-claim-delete",
        "object-bucket-claim-retain",
        "object-ec",
        "object-openshift",
        "object-test",
        "object-user",
        "object",
    ],
)
def test_object(filename):
    crd = load_example('object')
    c = CephObjectStore.from_json(crd)
    assert crd == c.to_json()


def test_nfs():
    crd = load_example('nfs')
    c = CephNFS.from_json(crd)
    assert crd == c.to_json()



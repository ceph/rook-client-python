import yaml

from rook_ceph_client.cephcluster import CephCluster
from rook_ceph_client.cephfilesystem import CephFilesystem
from rook_ceph_client.cephnfs import CephNFS
from rook_ceph_client.cephobjectstore import CephObjectStore


def load_example(what):
    with open(f'/home/sebastian/go/src/github.com/rook/rook/cluster/examples/kubernetes/ceph/{what}.yaml') as f:
        return yaml.safe_load(f.read())


def test_cluster():
    crd = load_example('cluster')
    c = CephCluster.from_json(crd)
    assert crd == c.to_json()


def test_cluster_test():
    crd = load_example('cluster-test')
    c = CephCluster.from_json(crd)
    assert crd == c.to_json()


def test_cluster_minimal():
    crd = load_example('cluster-minimal')
    c = CephCluster.from_json(crd)
    assert crd == c.to_json()


def test_filesystem():
    crd = load_example('filesystem')
    c = CephFilesystem.from_json(crd)
    assert crd == c.to_json()


def test_filesystem_ec():
    crd = load_example('filesystem-ec')
    c = CephFilesystem.from_json(crd)
    assert crd == c.to_json()


def test_filesystem_test():
    crd = load_example('filesystem-test')
    c = CephFilesystem.from_json(crd)
    assert crd == c.to_json()


def test_object():
    crd = load_example('object')
    c = CephObjectStore.from_json(crd)
    assert crd == c.to_json()


def test_object_ec():
    crd = load_example('object-ec')
    c = CephObjectStore.from_json(crd)
    assert crd == c.to_json()


def test_object_test():
    crd = load_example('object-test')
    c = CephObjectStore.from_json(crd)
    assert crd == c.to_json()


def test_nfs():
    crd = load_example('nfs')
    c = CephNFS.from_json(crd)
    assert crd == c.to_json()



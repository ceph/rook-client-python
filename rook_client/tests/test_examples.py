from os.path import expanduser

import yaml
import pytest

import rook_client
from rook_client.cassandra.cluster import Cluster as CassandraCluster
from rook_client.ceph.cephcluster import CephCluster
from rook_client.ceph.cephfilesystem import CephFilesystem
from rook_client.ceph.cephnfs import CephNFS
from rook_client.ceph.cephobjectstore import CephObjectStore
from rook_client.edgefs.cluster import Cluster as EdgefsCluster


def load_example(what):
    #import requests
    #url = f'https://raw.githubusercontent.com/rook/rook/master/cluster/examples/kubernetes/{what}'
    #r = requests.get(url, allow_redirects=True)
    #return r.content.decode('utf-8')

    with open(expanduser('~/go/src/github.com/rook/rook/cluster/examples/kubernetes/{what}').format(what=what)) as f:
        return f.read()

@pytest.mark.parametrize(
    "strict,cls,filename",
    [
        (True, CephCluster, "ceph/cluster-external.yaml"),
        (True, CephCluster, "ceph/cluster-minimal.yaml"),
        (True, CephCluster, "ceph/cluster-on-pvc.yaml"),
        (True, CephCluster, "ceph/cluster-test.yaml"),
        (True, CephCluster, "ceph/cluster.yaml"),
        (True, CephFilesystem, "ceph/filesystem-ec.yaml"),
        (True, CephFilesystem, "ceph/filesystem-test.yaml"),
        (True, CephFilesystem, "ceph/filesystem.yaml"),
        (True, CephObjectStore, "ceph/object-ec.yaml"),
        (True, CephObjectStore, "ceph/object-openshift.yaml"),
        (True, CephObjectStore, "ceph/object-test.yaml"),
        (True, CephObjectStore, "ceph/object.yaml"),
        (True, CephNFS, "ceph/nfs.yaml"),

        (False, CassandraCluster, "cassandra/cluster.yaml"),
        (False, EdgefsCluster, "edgefs/cluster.yaml"),
    ],
)
def test_exact_match(strict, cls, filename):
    crds = yaml.safe_load_all(load_example(filename))
    rook_client.STRICT = strict
    [crd] = [e for e in crds if e.get('kind', '') == cls.__name__]

    c = cls.from_json(crd)
    assert crd == c.to_json()





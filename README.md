# rook-ceph-client-python

Automatically generated models for Rook-Ceph's custom resource definitions.

Can be uased to type check client code against the Rook API

Inspired by https://github.com/kubernetes-client/python/tree/master/kubernetes/client/models


## Example

```python
def objectstore(api_name, name, namespace, instances):
    from rook_ceph_client import cephobjectstore as cos
    rook_os = cos.CephObjectStore(
        apiVersion=api_name,
        metadata=dict(
            name=name,
            namespace=namespace
        ),
        spec=cos.Spec(
            metadataPool=cos.MetadataPool(
                failureDomain='host',
                replicated=cos.Replicated(
                    size=1
                )
            ),
            dataPool=cos.DataPool(
                failureDomain='osd',
                replicated=cos.Replicated(
                    size=1
                )
            ),
            gateway=cos.Gateway(
                type='s3',
                port=80,
                instances=instances
            )
        )
    )
    return rook_os.to_json()
```

## Demo

![](rook-python-client-demo.gif)

## Regenerate

Re-generate the python files using 

```bash
python generate.py && python setup.py mkcodes && python setup.py test
```
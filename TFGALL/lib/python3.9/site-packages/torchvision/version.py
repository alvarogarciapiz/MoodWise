__version__ = '0.15.1'
git_version = '42759b1cc82bed60481c2802811595833e2ddd9b'
from torchvision.extension import _check_cuda_version
if _check_cuda_version() > 0:
    cuda = _check_cuda_version()

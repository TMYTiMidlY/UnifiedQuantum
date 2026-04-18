import warnings
from typing import TYPE_CHECKING
try:
    # uniq_cpp extension is implemented by C++
    from uniq_cpp import *
    if TYPE_CHECKING:
        from .uniq_cpp import *
except ImportError as e:
    # Note: Without compiling the UniqCpp, you can also use uniq.
    # Only the C++ simulator is disabled.
    warnings.warn('uniq is not install with UniqCpp.')

from .originir_simulator import OriginIR_Simulator, OriginIR_NoisySimulator
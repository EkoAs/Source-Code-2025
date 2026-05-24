# import RUMUS as RUMUS
# from . import RUMUS
# from .RUMUS.Progres import Math
# from .RUMUS.FaktorialRumus import Factorial
# from .RUMUS.TrinogomertyR import Trigonometry, TrigonometryBasic, TrinogomeOpsi
# from .RUMUS.MatrixRumus import Matrixs, MatrixInvers, MatrixsTranspose
# from .User import kalkulator_biasa, kalkulator_Trinogo,matrix_Math

# DATA/__init__.py
# Impor modul dari dalam paket DATA
from .User import kalkulator_biasa, kalkulator_Trinogo, matrix_Math, factorial_Opsi
# Impor kelas-kelas dari sub-paket RUMUS
from .RUMUS.Progres import Math
from .RUMUS.FaktorialRumus import Factorial
from .RUMUS.TrinogomertyR import Trigonometry, TrigonometryBasic, TrinogomeOpsi
from .RUMUS.MatrixRumus import Matrixs, MatrixInvers, MatrixsTranspose
from .RUMUS.BarisdanDeretR import BarisDeret
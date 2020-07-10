# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from typing import (
    Dict,
    Optional,
    Union,
)


def FF_critical_pressure_ratio_l(Psat: float, Pc: float) -> float: ...


def Reynolds_factor(FL: float, C: float, d: float, Rev: float, full_trim: bool = ...) -> float: ...


def Reynolds_valve(nu: float, Q: float, D1: float, FL: float, Fd: float, C: float) -> float: ...


def cavitation_index(P1: float, P2: float, Psat: float) -> float: ...


def control_valve_choke_P_g(xT: float, gamma: float, P1: Optional[float] = ..., P2: Optional[float] = ...) -> float: ...


def control_valve_choke_P_l(
    Psat: float,
    Pc: float,
    FL: float,
    P1: Optional[float] = ...,
    P2: Optional[float] = ...,
    disp: bool = ...
) -> float: ...


def control_valve_noise_g_2011(
    m: float,
    P1: float,
    P2: float,
    T1: int,
    rho: float,
    gamma: float,
    MW: float,
    Kv: float,
    d: float,
    Di: float,
    t_pipe: float,
    Fd: float,
    FL: None,
    FLP: Optional[float] = ...,
    FP: Optional[float] = ...,
    rho_pipe: float = ...,
    c_pipe: float = ...,
    P_air: float = ...,
    rho_air: float = ...,
    c_air: float = ...,
    An: float = ...,
    Stp: float = ...,
    T2: None = ...,
    beta: float = ...
) -> float: ...


def control_valve_noise_l_2015(
    m: int,
    P1: float,
    P2: float,
    Psat: float,
    rho: float,
    c: float,
    Kv: float,
    d: float,
    Di: float,
    FL: float,
    Fd: float,
    t_pipe: float,
    rho_pipe: float = ...,
    c_pipe: float = ...,
    rho_air: float = ...,
    c_air: float = ...,
    xFz: Optional[float] = ...,
    An: float = ...
) -> float: ...


def is_choked_turbulent_g(x: float, Fgamma: float, xT: Optional[float] = ..., xTP: Optional[float] = ...) -> bool: ...


def is_choked_turbulent_l(
    dP: float,
    P1: float,
    Psat: float,
    FF: float,
    FL: Optional[float] = ...,
    FLP: Optional[float] = ...,
    FP: Optional[float] = ...
) -> bool: ...


def loss_coefficient_piping(d: float, D1: Optional[float] = ..., D2: Optional[float] = ...) -> float: ...


def size_control_valve_g(
    T: float,
    MW: float,
    mu: float,
    gamma: float,
    Z: float,
    P1: float,
    P2: float,
    Q: float,
    D1: Optional[float] = ...,
    D2: Optional[float] = ...,
    d: Optional[float] = ...,
    FL: float = ...,
    Fd: float = ...,
    xT: float = ...,
    allow_choked: bool = ...,
    allow_laminar: bool = ...,
    full_output: bool = ...
) -> Union[Dict[str, Optional[Union[bool, float]]], float, Dict[str, Optional[Union[float, bool, str]]]]: ...


def size_control_valve_l(
    rho: float,
    Psat: float,
    Pc: float,
    mu: float,
    P1: float,
    P2: float,
    Q: float,
    D1: Optional[float] = ...,
    D2: Optional[float] = ...,
    d: Optional[float] = ...,
    FL: float = ...,
    Fd: float = ...,
    allow_choked: bool = ...,
    allow_laminar: bool = ...,
    full_output: bool = ...
) -> Union[float, Dict[str, Optional[Union[bool, float]]], Dict[str, Optional[Union[float, bool, str]]]]: ...

__all__: List[str]
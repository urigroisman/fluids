# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from typing import (
    List,
    Optional,
    Union,
)


def Cv_to_K(Cv: float, D: float) -> float: ...


def Cv_to_Kv(Cv: float) -> float: ...


def Darby3K(
    NPS: Optional[float] = ...,
    Re: Optional[float] = ...,
    name: Optional[str] = ...,
    K1: Optional[float] = ...,
    Ki: Optional[float] = ...,
    Kd: Optional[float] = ...
) -> float: ...


def Hooper2K(
    Di: float,
    Re: float,
    name: Optional[str] = ...,
    K1: Optional[float] = ...,
    Kinfty: Optional[float] = ...
) -> float: ...


def K_angle_stop_check_valve_Crane(D1: float, D2: float, fd: Optional[float] = ..., style: int = ...) -> float: ...


def K_angle_valve_Crane(D1: float, D2: float, fd: Optional[float] = ..., style: int = ...) -> float: ...


def K_ball_valve_Crane(D1: float, D2: float, angle: float, fd: Optional[float] = ...) -> float: ...


def K_branch_converging_Crane(
    D_run: float,
    D_branch: float,
    Q_run: float,
    Q_branch: float,
    angle: float = ...
) -> float: ...


def K_branch_diverging_Crane(
    D_run: float,
    D_branch: float,
    Q_run: float,
    Q_branch: float,
    angle: float = ...
) -> float: ...


def K_butterfly_valve_Crane(D: float, fd: Optional[float] = ..., style: int = ...) -> float: ...


def K_diaphragm_valve_Crane(D: Optional[float] = ..., fd: Optional[float] = ..., style: int = ...) -> float: ...


def K_foot_valve_Crane(D: Optional[float] = ..., fd: Optional[float] = ..., style: int = ...) -> float: ...


def K_gate_valve_Crane(D1: float, D2: float, angle: float, fd: Optional[float] = ...) -> float: ...


def K_globe_stop_check_valve_Crane(D1: float, D2: float, fd: Optional[float] = ..., style: int = ...) -> float: ...


def K_globe_valve_Crane(D1: float, D2: float, fd: Optional[float] = ...) -> float: ...


def K_lift_check_valve_Crane(D1: float, D2: float, fd: Optional[float] = ..., angled: bool = ...) -> float: ...


def K_plug_valve_Crane(
    D1: float,
    D2: float,
    angle: float,
    fd: Optional[float] = ...,
    style: int = ...
) -> float: ...


def K_run_converging_Crane(
    D_run: float,
    D_branch: float,
    Q_run: float,
    Q_branch: float,
    angle: float = ...
) -> float: ...


def K_run_diverging_Crane(
    D_run: float,
    D_branch: float,
    Q_run: float,
    Q_branch: float,
    angle: float = ...
) -> float: ...


def K_swing_check_valve_Crane(D: Optional[float] = ..., fd: Optional[float] = ..., angled: bool = ...) -> float: ...


def K_tilting_disk_check_valve_Crane(D: float, angle: float, fd: Optional[float] = ...) -> float: ...


def K_to_Cv(K: float, D: float) -> float: ...


def K_to_Kv(K: float, D: float) -> float: ...


def Kv_to_Cv(Kv: float) -> float: ...


def Kv_to_K(Kv: float, D: float) -> float: ...


def Miller_bend_roughness_correction(Re: float, Di: float, roughness: float) -> float: ...


def Miller_bend_unimpeded_correction(Kb: float, Di: float, L_unimpeded: float) -> float: ...


def bend_miter(
    angle: float,
    Di: Optional[float] = ...,
    Re: Optional[float] = ...,
    roughness: float = ...,
    L_unimpeded: Optional[float] = ...,
    method: str = ...
) -> float: ...


def bend_miter_Miller(
    Di: float,
    angle: float,
    Re: float,
    roughness: float = ...,
    L_unimpeded: Optional[float] = ...
) -> float: ...


def bend_rounded(
    Di: float,
    angle: float,
    fd: Optional[float] = ...,
    rc: Optional[float] = ...,
    bend_diameters: float = ...,
    Re: Optional[float] = ...,
    roughness: float = ...,
    L_unimpeded: None = ...,
    method: str = ...
) -> float: ...


def bend_rounded_Crane(
    Di: float,
    angle: float,
    rc: Optional[float] = ...,
    bend_diameters: Optional[float] = ...
) -> float: ...


def bend_rounded_Ito(
    Di: float,
    angle: int,
    Re: float,
    rc: Optional[float] = ...,
    bend_diameters: Optional[float] = ...,
    roughness: float = ...
) -> float: ...


def bend_rounded_Miller(
    Di: float,
    angle: int,
    Re: float,
    rc: Optional[float] = ...,
    bend_diameters: Optional[float] = ...,
    roughness: float = ...,
    L_unimpeded: Optional[float] = ...
) -> float: ...


def change_K_basis(K1: float, D1: float, D2: float) -> float: ...


def contraction_beveled(Di1: float, Di2: float, l: Optional[float] = ..., angle: Optional[float] = ...) -> float: ...


def contraction_conical(
    Di1: float,
    Di2: float,
    fd: Optional[float] = ...,
    l: Optional[float] = ...,
    angle: Optional[float] = ...,
    Re: Optional[float] = ...,
    roughness: float = ...,
    method: str = ...
) -> float: ...


def contraction_conical_Crane(
    Di1: float,
    Di2: float,
    l: Optional[float] = ...,
    angle: Optional[float] = ...
) -> float: ...


def contraction_round(Di1: float, Di2: float, rc: float, method: str = ...) -> float: ...


def contraction_round_Miller(Di1: float, Di2: float, rc: float) -> float: ...


def contraction_sharp(Di1: int, Di2: float) -> float: ...


def diffuser_conical(
    Di1: float,
    Di2: float,
    l: Optional[float] = ...,
    angle: Optional[float] = ...,
    fd: Optional[float] = ...,
    Re: Optional[float] = ...,
    roughness: float = ...,
    method: str = ...
) -> float: ...


def diffuser_conical_staged(
    Di1: float,
    Di2: float,
    DEs: List[float],
    ls: List[float],
    fd: Optional[float] = ...,
    method: str = ...
) -> float: ...


def diffuser_curved(Di1: float, Di2: float, l: float) -> float: ...


def diffuser_pipe_reducer(Di1: float, Di2: float, l: float, fd1: float, fd2: Optional[float] = ...) -> float: ...


def diffuser_sharp(Di1: float, Di2: float) -> float: ...


def entrance_angled(angle: float, method: str = ...) -> float: ...


def entrance_beveled(Di: float, l: float, angle: float, method: str = ...) -> float: ...


def entrance_beveled_orifice(Di: float, do: float, l: float, angle: float) -> float: ...


def entrance_distance(Di: float, t: Optional[float] = ..., l: Optional[float] = ..., method: str = ...) -> float: ...


def entrance_distance_45_Miller(Di: float, Di0: float) -> float: ...


def entrance_rounded(Di: float, rc: float, method: str = ...) -> float: ...


def entrance_sharp(method: str = ...) -> float: ...


def exit_normal() -> float: ...


def helix(Di: float, rs: float, pitch: float, N: int, fd: float) -> float: ...


def spiral(Di: float, rmax: float, rmin: float, pitch: float, fd: float) -> float: ...


def v_lift_valve_Crane(rho: float, D1: Optional[float] = ..., D2: Optional[float] = ..., style: str = ...) -> float: ...

__all__: List[str]
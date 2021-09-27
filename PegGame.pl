%Six pegs in a line. Simulate one line of jumps.
:- dynamic in/2.

in(peg0, hole0).
in(peg1,hole1).
in(peg2,hole2).
in(empty,hole3).
in(peg4,hole4).
in(peg5,hole5).
in(peg6,hole6).


adjacent(hole0, hole1).

adjacent(hole1, hole0).
adjacent(hole1, hole2).

adjacent(hole2, hole1).
adjacent(hole2, hole3).

adjacent(hole3, hole2).
adjacent(hole3, hole4).

adjacent(hole4, hole3).
adjacent(hole4, hole5).

adjacent(hole5, hole4).
adjacent(hole5, hole6).

adjacent(hole6, hole5).



can_jump(P1, P2, H) :-
    P1 \== P2,
    in(P1, X),
    in(P2, Y),
    in(P3,H),
    P3 == empty,
    P1 \== empty,
    P2 \== empty,
    X \== Y,
    X \== H,
    adjacent(X,Y),
    adjacent(Y,H).

jump(P1,P2,H) :-
    can_jump(P1,P2,H),
    out(P1,P2,H),
    retract(in(P1,X)),
    retract(in(P2,Y)),
    retract(in(empty,H)),
    assert(in(P1,H)),
    assert(in(empty,X)),
    assert(in(empty,Y)).

out(P1,P2,H) :-
    write('Jump '),
    write(P1),
    write(' over '),
    write(P2),
    write(' into '),
    write(H).

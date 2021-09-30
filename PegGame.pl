%A full 15 peg Crazy Triangle representation.
:- dynamic in/2.

%Bottom - Layer 0.
in(peg0, hole00).
in(peg1,hole01).
in(peg2,hole02).
in(peg3,hole03).
in(peg4,hole04).

%Layer 1.
in(peg5, hole10).
in(peg6,hole11).
in(peg7,hole12).
in(peg8,hole13).

%Layer 2.
in(peg9, hole20).
in(peg10,hole21).
in(peg11,hole22).

%Layer 3.
in(peg12,hole30).
in(peg13,hole31).

%Top - Layer 4.
in(empty,hole40).

%Row-wise adjacency.
%Layer 0.
adjacent(hole00, hole01).
adjacent(hole01, hole00).
adjacent(hole01, hole02).
adjacent(hole02, hole01).
adjacent(hole02, hole03).
adjacent(hole03, hole02).
adjacent(hole03, hole04).
adjacent(hole04, hole03).

%Layer 1.
adjacent(hole10, hole11).
adjacent(hole11, hole10).
adjacent(hole11, hole12).
adjacent(hole12, hole11).
adjacent(hole12, hole13).
adjacent(hole13, hole12).

%Layer 2.
adjacent(hole20, hole21).
adjacent(hole21, hole20).
adjacent(hole21, hole22).
adjacent(hole22, hole21).

%Layer 3.
adjacent(hole30, hole31).
adjacent(hole31, hole30).

%Column-wise adjacency.
% Since pegs live between pegs on higher layers, we can jump vertically
% left or right. LCol = (Col, Row-1) and RCol = (Col+1, Row-1).
% Must jump from left adjacent to the right adjacent or the right
% adjacent to left adjacent.

%Left adjacency
l_adjacent(hole01, hole10).
l_adjacent(hole02, hole11).
l_adjacent(hole03, hole12).
l_adjacent(hole04, hole13).

l_adjacent(hole11, hole20).
l_adjacent(hole12, hole21).
l_adjacent(hole13, hole22).

l_adjacent(hole21, hole30).
l_adjacent(hole22, hole31).

l_adjacent(hole31, hole40).

%test
ld_adjacent(hole10, hole00).
ld_adjacent(hole11, hole01).
ld_adjacent(hole12, hole02).
ld_adjacent(hole13, hole03).

ld_adjacent(hole20, hole10).
ld_adjacent(hole21, hole11).
ld_adjacent(hole22, hole12).

ld_adjacent(hole30, hole20).
ld_adjacent(hole31, hole21).

ld_adjacent(hole40, hole30).

%Right adjacency
r_adjacent(hole00, hole10).
r_adjacent(hole01, hole11).
r_adjacent(hole02, hole12).
r_adjacent(hole03, hole13).

r_adjacent(hole10, hole20).
r_adjacent(hole11, hole21).
r_adjacent(hole12, hole22).

r_adjacent(hole20, hole30).
r_adjacent(hole21, hole31).

r_adjacent(hole30, hole40).

%test
rd_adjacent(hole10, hole01).
rd_adjacent(hole11, hole02).
rd_adjacent(hole12, hole03).
rd_adjacent(hole13, hole04).

rd_adjacent(hole20, hole11).
rd_adjacent(hole21, hole12).
rd_adjacent(hole22, hole13).

rd_adjacent(hole30, hole20).
rd_adjacent(hole31, hole22).

rd_adjacent(hole40, hole31).



can_jump(P1, P2, H) :-
    can_jump_h(P1,P2,H);
    can_jump_vl(P1,P2,H);
    can_jump_vr(P1,P2,H).

can_jump_vl(P1, P2, H):-
    P1 \== P2,
    in(P1, X),
    in(P2, Y),
    in(P3,H),
    P3 == empty,
    P1 \== empty,
    P2 \== empty,
    X \== Y,
    X \== H,
    (l_adjacent(X,Y),l_adjacent(Y,H);
    ld_adjacent(X,Y),ld_adjacent(Y,H)).

can_jump_vr(P1, P2, H):-
    P1 \== P2,
    in(P1, X),
    in(P2, Y),
    in(P3,H),
    P3 == empty,
    P1 \== empty,
    P2 \== empty,
    X \== Y,
    X \== H,
    (r_adjacent(X,Y),r_adjacent(Y,H);
    rd_adjacent(X,Y),rd_adjacent(Y,H)).

can_jump_h(P1, P2, H):-
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
    in(P1,X),
    in(P2,Y),
    write('Jump peg in '),
    write(X),
    write(' over '),
    write(Y),
    write(' into '),
    write(H), write('\n').

play(1):-write('Only one left! Win!'),nl.
play(N):-
    N>1,
    jump(P1,P2,H),
    S is N-1,
    play(S).



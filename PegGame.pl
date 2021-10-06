%A full 15 peg Crazy Triangle representation.
:- dynamic in/2, adjacent/2,
    l_adjacent/2,  ld_adjacent/2,  r_adjacent/2, rd_adjacent/2.

%Deletes all associations between pegs and holes.
%Creates new atoms for peg and hole.
%Deletes all associations in the adjacency matrix.
%Creates new atoms needed for adjacency matrix.
%N = Max number of rows.

refresh_game(N):-
    %Subtract to index at 0.
    N2 is N-1,

    %Retracting predicates.
    retractall(in(_,_)),
    retractall(adjacent(_,_)),
    retractall(l_adjacent(_,_)),
    retractall(ld_adjacent(_,_)),
    retractall(r_adjacent(_,_)),
    retractall(rd_adjacent(_,_)),

    %Define empty hole.
    atom_concat(hole,N2,Hole),
    atom_concat(Hole,0,Hole2),
    assert(in(empty,Hole2)),

    %Special case facts
    H is N2 - 1,
    atom_concat(hole,H,Hole3),
    atom_concat(Hole3,0,Hole4),
    assert(ld_adjacent(Hole2,Hole4)),
    assert(r_adjacent(Hole4,Hole2)),
    atom_concat(Hole3,1,Hole5),
    assert(rd_adjacent(Hole2,Hole5)),

    %Adjacency matrix and peg generation.
    N3 is N2-1,
    between(0,N3,X), %TODO: Combine between clauses with forall
    Q is N2-X,
    between(0,Q,Y),
    set_in(X,Y),
    set_adjacent(X,Y),
    set_l_adjacent(X,Y),
    set_ld_adjacent(X,Y),
    set_r_adjacent(X,Y),
    set_rd_adjacent(X,Y).

%Initializing all in(Peg,Hole).
set_in(N,M):-
    atom_concat(peg,N,Peg),
    atom_concat(hole,N,Hole),
    atom_concat(Peg,M,Peg2),
    atom_concat(Hole,M,Hole2),
    assert(in(Peg2,Hole2)).

%Initialize horizontal adjacency.
set_adjacent(N,M):-
    (atom_concat(hole,N,Hole1),
    atom_concat(hole,N,Hole2),
    atom_concat(Hole1,M,Hole1_2),
    M2 is M - 1,
    M2>=0,
    atom_concat(Hole2,M2,Hole2_2),
    assert(adjacent(Hole1_2,Hole2_2)),
    assert(adjacent(Hole2_2,Hole1_2)));true.

%Initialize left horizontal adjacency.
set_l_adjacent(N,M):-
    (atom_concat(hole,N,Hole1),
    atom_concat(Hole1,M,Hole1_2),
    N2 is N + 1,
    M2 is M - 1,
    M2 >= 0,
    atom_concat(hole,N2,Hole2),
    atom_concat(Hole2,M2,Hole2_2),
    \+ l_adjacent(Hole1_2, Hole2_2),
    assert(l_adjacent(Hole1_2,Hole2_2)));true.

%Initialize right horizontal adjacency
set_r_adjacent(N,M):-
    (atom_concat(hole,N,Hole1),
    atom_concat(Hole1,M,Hole1_2),
    N2 is N - 1,
    N2 >= 0,
    atom_concat(hole,N2,Hole2),
    atom_concat(Hole2,M,Hole2_2),
    \+ r_adjacent(Hole2_2, Hole1_2),
    assert(r_adjacent(Hole2_2,Hole1_2)));true.

%Initialize left downward horizontal adjacency.
set_ld_adjacent(N,M):-
    (atom_concat(hole,N,Hole1),
    atom_concat(Hole1,M,Hole1_2),
    N2 is N - 1,
    N2 >= 0,
    atom_concat(hole,N2,Hole2),
    atom_concat(Hole2,M,Hole2_2),
    \+ ld_adjacent(Hole1_2, Hole2_2),
    assert(ld_adjacent(Hole1_2,Hole2_2)));true.

%Initialize right downward horizontal adjacency.
set_rd_adjacent(N,M):-
    (atom_concat(hole,N,Hole1),
    atom_concat(Hole1,M,Hole1_2),
    N2 is N - 1,
    M2 is M + 1,
    N2 >= 0,
    atom_concat(hole,N2,Hole2),
    atom_concat(Hole2,M2,Hole2_2),
    \+ rd_adjacent(Hole1_2, Hole2_2),
    assert(rd_adjacent(Hole1_2,Hole2_2)));true.

%Checks for jumps in all directions.
can_jump(P1, P2, H) :-
    can_jump_h(P1,P2,H);
    can_jump_vr(P1,P2,H);
    can_jump_vl(P1,P2,H).

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

%Notify of jump and update facts.
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

%Plays game until one peg remains, or when no jumps remain.
play(1):-write('Only one left! Win!'),nl.
play(N):-
    N>1,
    jump(P1,P2,H),
    S is N-1,
    play(S).










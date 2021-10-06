(define (problem ThreePegs) (:domain TRICKY_TRIANGLE)
    (:objects p1 p2 h1 h2 h3)

    (:init
        (peg p1)
        (peg p2)
        (hole h1)
        (hole h2)
        (hole h3)
        (in p1 h1)
        (in p2 h2)
    )

    (:goal (and (in p1 h3)))
)

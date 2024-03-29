(define (problem ThreePegs) (:domain TRICKY_TRIANGLE)
    (:objects p1 p2 p4 p5 p6 p7 p8 p9 p10 h1 h2 h3 h4 h5 h6 h7 h8 h9 h10)
    (:init
        (peg p1) (peg p2) (peg p4) (peg p5) (peg p6) (peg p7) (peg p8) (peg p9) (peg p10)
        (hole h1) (hole h2) (hole h3) (hole h4) (hole h5) (hole h6) (hole h7) (hole h8) (hole h9) (hole h10)
        (empty-hole h2)
        (in p1 h1) (in p2 h2) (in p4 h4) (in p5 h5) (in p6 h6) (in p7 h7) (in p8 h8) (in p9 h9) (in p10 h10)
        (adjacent h1 h2) (adjacent h1 h4)
        (adjacent h2 h1) (adjacent h2 h5) (adjacent h2 h3)
        (adjacent h3 h2) (adjacent h3 h5) (adjacent h3 h7)
        (adjacent h4 h1) (adjacent h4 h5) (adjacent h4 h6)
        (adjacent h5 h4) (adjacent h5 h2) (adjacent h5 h3) (adjacent h5 h6) (adjacent h5 h8) (adjacent h5 h9)
        (adjacent h6 h4) (adjacent h6 h5) (adjacent h6 h10)
        (adjacent h7 h3) (adjacent h7 h8)
        (adjacent h8 h7) (adjacent h8 h5) (adjacent h8 h9)
        (adjacent h9 h5) (adjacent h9 h8) (adjacent h9 h10)
        (adjacent h10 h6) (adjacent h10 h9)
        (in-line h1 h2 h3) (in-line h3 h2 h1)
        (in-line h2 h3 h7) (in-line h7 h3 h2)
        (in-line h1 h4 h6) (in-line h6 h4 h1)
        (in-line h4 h6 h10) (in-line h10 h6 h4)
        (in-line h3 h5 h6) (in-line h6 h5 h3)
        (in-line h2 h5 h9) (in-line h9 h5 h2)
        (in-line h4 h5 h8) (in-line h8 h5 h4)
        (in-line h7 h8 h9) (in-line h9 h8 h7)
        (in-line h8 h9 h10) (in-line h10 h9 h8)
    )

    (:goal  
        (and 
            (empty-hole h1)
            (empty-hole h2)
            (empty-hole h3)
            (empty-hole h4)
            (empty-hole h5)
            (empty-hole h6)
            
            (empty-hole h8)
            (empty-hole h9)
            (empty-hole h10)
        )
    )
)
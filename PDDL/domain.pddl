(define (domain TRICKY_TRIANGLE)

    (:requirements :negative-preconditions)
    (:predicates
        (peg ?p)
        (hole ?h)
        (in ?p ?h)
        (adjacent ?hole1 ?hole2)
        (empty-hole ?hole-name)
    )

    (:action jump
        :parameters (?moving-peg ?over-peg ?source-hole ?over-hole ?destination-hole)
        :precondition   (and (peg ?moving-peg) (peg ?over-peg) 
                            (hole ?over-hole) (hole ?source-hole) (hole ?destination-hole)
                            (in ?moving-peg ?source-hole) (in ?over-peg ?over-hole)
                            (adjacent ?source-hole ?over-hole) (adjacent ?over-hole ?destination-hole)
                            (empty-hole ?destination-hole)
                            (not (in ?moving-peg ?over-hole))
                        )
        :effect (and (in ?moving-peg ?destination-hole) 
                    (not (empty-hole ?destination-hole))
                    (not (in ?moving-peg ?source-hole)) 
                    (not (in ?over-peg ?over-hole)))
    )
)
    
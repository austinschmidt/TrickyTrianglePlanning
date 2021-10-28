(define (problem line5_0_1)
(:domain pegs)
(:objects 
	p0 h0 p1 h1 p2 h2 p3 h3 h4 )
(:init
	(empty h0)
	(in p0 h1)
	(in p1 h2)
	(in p2 h3)
	(in p3 h4)
	(adjacent h0 h1)
	(adjacent h1 h0)
	(adjacent h1 h2)
	(adjacent h2 h1)
	(adjacent h2 h3)
	(adjacent h3 h2)
	(adjacent h3 h4)
	(adjacent h4 h3)
	(inline h0 h1 h2)
	(inline h2 h1 h0)
	(inline h1 h2 h3)
	(inline h3 h2 h1)
	(inline h2 h3 h4)
	(inline h4 h3 h2))
(:goal (and 
	(empty h0)
	(empty h2)
	(empty h3)
	(empty h4)
)))
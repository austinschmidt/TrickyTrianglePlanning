(define (problem square3_3_4)
(:domain pegs)
(:objects 
	p0 h0 p1 h1 p2 h2 p3 h3 p4 h4 p5 h5 p6 h6 p7 h7 h8 )
(:init
	(empty h3)
	(in p0 h0)
	(in p1 h1)
	(in p2 h2)
	(in p3 h4)
	(in p4 h5)
	(in p5 h6)
	(in p6 h7)
	(in p7 h8)
	(adjacent h0 h1)
	(adjacent h1 h0)
	(adjacent h0 h3)
	(adjacent h3 h0)
	(adjacent h1 h2)
	(adjacent h2 h1)
	(adjacent h1 h4)
	(adjacent h4 h1)
	(adjacent h2 h5)
	(adjacent h5 h2)
	(adjacent h3 h4)
	(adjacent h4 h3)
	(adjacent h3 h6)
	(adjacent h6 h3)
	(adjacent h4 h5)
	(adjacent h5 h4)
	(adjacent h4 h7)
	(adjacent h7 h4)
	(adjacent h5 h8)
	(adjacent h8 h5)
	(adjacent h6 h7)
	(adjacent h7 h6)
	(adjacent h7 h8)
	(adjacent h8 h7)
	(inline h0 h1 h2)
	(inline h2 h1 h0)
	(inline h0 h3 h6)
	(inline h6 h3 h0)
	(inline h1 h4 h7)
	(inline h7 h4 h1)
	(inline h2 h5 h8)
	(inline h8 h5 h2)
	(inline h3 h4 h5)
	(inline h5 h4 h3)
	(inline h6 h7 h8)
	(inline h8 h7 h6)
)
(:goal (and 
	(empty h0)
	(empty h1)
	(empty h2)
	(empty h3)
	(empty h5)
	(empty h6)
	(empty h7)
	(empty h8)
)))
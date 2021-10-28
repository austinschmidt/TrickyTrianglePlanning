(define (problem triangle5_5_7)
(:domain pegs)
(:objects 
	p0 h0 p1 h1 p2 h2 p3 h3 p4 h4 p5 h5 p6 h6 p7 h7 p8 h8 p9 h9 
	p10 h10 p11 h11 p12 h12 p13 h13 h14 )
(:init
	(empty h5)
	(in p0 h0)
	(in p1 h1)
	(in p2 h2)
	(in p3 h3)
	(in p4 h4)
	(in p5 h6)
	(in p6 h7)
	(in p7 h8)
	(in p8 h9)
	(in p9 h10)
	(in p10 h11)
	(in p11 h12)
	(in p12 h13)
	(in p13 h14)
	(adjacent h0 h1)
	(adjacent h1 h0)
	(adjacent h0 h5)
	(adjacent h5 h0)
	(adjacent h1 h2)
	(adjacent h2 h1)
	(adjacent h1 h5)
	(adjacent h5 h1)
	(adjacent h1 h6)
	(adjacent h6 h1)
	(adjacent h2 h3)
	(adjacent h3 h2)
	(adjacent h2 h6)
	(adjacent h6 h2)
	(adjacent h2 h7)
	(adjacent h7 h2)
	(adjacent h3 h4)
	(adjacent h4 h3)
	(adjacent h3 h7)
	(adjacent h7 h3)
	(adjacent h3 h8)
	(adjacent h8 h3)
	(adjacent h4 h8)
	(adjacent h8 h4)
	(adjacent h5 h6)
	(adjacent h6 h5)
	(adjacent h5 h9)
	(adjacent h9 h5)
	(adjacent h6 h7)
	(adjacent h7 h6)
	(adjacent h6 h9)
	(adjacent h9 h6)
	(adjacent h6 h10)
	(adjacent h10 h6)
	(adjacent h7 h8)
	(adjacent h8 h7)
	(adjacent h7 h10)
	(adjacent h10 h7)
	(adjacent h7 h11)
	(adjacent h11 h7)
	(adjacent h8 h11)
	(adjacent h11 h8)
	(adjacent h9 h10)
	(adjacent h10 h9)
	(adjacent h9 h12)
	(adjacent h12 h9)
	(adjacent h10 h11)
	(adjacent h11 h10)
	(adjacent h10 h12)
	(adjacent h12 h10)
	(adjacent h10 h13)
	(adjacent h13 h10)
	(adjacent h11 h13)
	(adjacent h13 h11)
	(adjacent h12 h13)
	(adjacent h13 h12)
	(adjacent h12 h14)
	(adjacent h14 h12)
	(adjacent h13 h14)
	(adjacent h14 h13)
	(inline h0 h1 h2)
	(inline h2 h1 h0)
	(inline h0 h5 h9)
	(inline h9 h5 h0)
	(inline h1 h2 h3)
	(inline h3 h2 h1)
	(inline h1 h6 h10)
	(inline h10 h6 h1)
	(inline h2 h3 h4)
	(inline h4 h3 h2)
	(inline h2 h6 h9)
	(inline h9 h6 h2)
	(inline h2 h7 h11)
	(inline h11 h7 h2)
	(inline h3 h7 h10)
	(inline h10 h7 h3)
	(inline h4 h8 h11)
	(inline h11 h8 h4)
	(inline h5 h6 h7)
	(inline h7 h6 h5)
	(inline h5 h9 h12)
	(inline h12 h9 h5)
	(inline h6 h7 h8)
	(inline h8 h7 h6)
	(inline h6 h10 h13)
	(inline h13 h10 h6)
	(inline h7 h10 h12)
	(inline h12 h10 h7)
	(inline h8 h11 h13)
	(inline h13 h11 h8)
	(inline h9 h10 h11)
	(inline h11 h10 h9)
	(inline h9 h12 h14)
	(inline h14 h12 h9)
	(inline h11 h13 h14)
	(inline h14 h13 h11)
)
(:goal (and 
	(empty h0)
	(empty h1)
	(empty h2)
	(empty h3)
	(empty h4)
	(empty h5)
	(empty h6)
	(empty h8)
	(empty h9)
	(empty h10)
	(empty h11)
	(empty h12)
	(empty h13)
	(empty h14)
)))
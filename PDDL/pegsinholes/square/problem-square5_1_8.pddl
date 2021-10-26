(define (problem square5_1_8)
(:domain pegs)
(:objects 
	p0 h0 p1 h1 p2 h2 p3 h3 p4 h4 p5 h5 p6 h6 p7 h7 p8 h8 p9 h9 
	p10 h10 p11 h11 p12 h12 p13 h13 p14 h14 p15 h15 p16 h16 p17 h17 p18 h18 p19 h19 
	p20 h20 p21 h21 p22 h22 p23 h23 h24 )
(:init
	(empty h1)
	(in p0 h0)
	(in p1 h2)
	(in p2 h3)
	(in p3 h4)
	(in p4 h5)
	(in p5 h6)
	(in p6 h7)
	(in p7 h8)
	(in p8 h9)
	(in p9 h10)
	(in p10 h11)
	(in p11 h12)
	(in p12 h13)
	(in p13 h14)
	(in p14 h15)
	(in p15 h16)
	(in p16 h17)
	(in p17 h18)
	(in p18 h19)
	(in p19 h20)
	(in p20 h21)
	(in p21 h22)
	(in p22 h23)
	(in p23 h24)
	(adjacent h0 h1)
	(adjacent h1 h0)
	(adjacent h0 h5)
	(adjacent h5 h0)
	(adjacent h1 h2)
	(adjacent h2 h1)
	(adjacent h1 h6)
	(adjacent h6 h1)
	(adjacent h2 h3)
	(adjacent h3 h2)
	(adjacent h2 h7)
	(adjacent h7 h2)
	(adjacent h3 h4)
	(adjacent h4 h3)
	(adjacent h3 h8)
	(adjacent h8 h3)
	(adjacent h4 h9)
	(adjacent h9 h4)
	(adjacent h5 h6)
	(adjacent h6 h5)
	(adjacent h5 h10)
	(adjacent h10 h5)
	(adjacent h6 h7)
	(adjacent h7 h6)
	(adjacent h6 h11)
	(adjacent h11 h6)
	(adjacent h7 h8)
	(adjacent h8 h7)
	(adjacent h7 h12)
	(adjacent h12 h7)
	(adjacent h8 h9)
	(adjacent h9 h8)
	(adjacent h8 h13)
	(adjacent h13 h8)
	(adjacent h9 h14)
	(adjacent h14 h9)
	(adjacent h10 h11)
	(adjacent h11 h10)
	(adjacent h10 h15)
	(adjacent h15 h10)
	(adjacent h11 h12)
	(adjacent h12 h11)
	(adjacent h11 h16)
	(adjacent h16 h11)
	(adjacent h12 h13)
	(adjacent h13 h12)
	(adjacent h12 h17)
	(adjacent h17 h12)
	(adjacent h13 h14)
	(adjacent h14 h13)
	(adjacent h13 h18)
	(adjacent h18 h13)
	(adjacent h14 h19)
	(adjacent h19 h14)
	(adjacent h15 h16)
	(adjacent h16 h15)
	(adjacent h15 h20)
	(adjacent h20 h15)
	(adjacent h16 h17)
	(adjacent h17 h16)
	(adjacent h16 h21)
	(adjacent h21 h16)
	(adjacent h17 h18)
	(adjacent h18 h17)
	(adjacent h17 h22)
	(adjacent h22 h17)
	(adjacent h18 h19)
	(adjacent h19 h18)
	(adjacent h18 h23)
	(adjacent h23 h18)
	(adjacent h19 h24)
	(adjacent h24 h19)
	(adjacent h20 h21)
	(adjacent h21 h20)
	(adjacent h21 h22)
	(adjacent h22 h21)
	(adjacent h22 h23)
	(adjacent h23 h22)
	(adjacent h23 h24)
	(adjacent h24 h23)
	(inline h0 h1 h2)
	(inline h2 h1 h0)
	(inline h0 h5 h10)
	(inline h10 h5 h0)
	(inline h1 h2 h3)
	(inline h3 h2 h1)
	(inline h1 h6 h11)
	(inline h11 h6 h1)
	(inline h2 h3 h4)
	(inline h4 h3 h2)
	(inline h2 h7 h12)
	(inline h12 h7 h2)
	(inline h3 h8 h13)
	(inline h13 h8 h3)
	(inline h4 h9 h14)
	(inline h14 h9 h4)
	(inline h5 h6 h7)
	(inline h7 h6 h5)
	(inline h5 h10 h15)
	(inline h15 h10 h5)
	(inline h6 h7 h8)
	(inline h8 h7 h6)
	(inline h6 h11 h16)
	(inline h16 h11 h6)
	(inline h7 h8 h9)
	(inline h9 h8 h7)
	(inline h7 h12 h17)
	(inline h17 h12 h7)
	(inline h8 h13 h18)
	(inline h18 h13 h8)
	(inline h9 h14 h19)
	(inline h19 h14 h9)
	(inline h10 h11 h12)
	(inline h12 h11 h10)
	(inline h10 h15 h20)
	(inline h20 h15 h10)
	(inline h11 h12 h13)
	(inline h13 h12 h11)
	(inline h11 h16 h21)
	(inline h21 h16 h11)
	(inline h12 h13 h14)
	(inline h14 h13 h12)
	(inline h12 h17 h22)
	(inline h22 h17 h12)
	(inline h13 h18 h23)
	(inline h23 h18 h13)
	(inline h14 h19 h24)
	(inline h24 h19 h14)
	(inline h15 h16 h17)
	(inline h17 h16 h15)
	(inline h16 h17 h18)
	(inline h18 h17 h16)
	(inline h17 h18 h19)
	(inline h19 h18 h17)
	(inline h20 h21 h22)
	(inline h22 h21 h20)
	(inline h21 h22 h23)
	(inline h23 h22 h21)
	(inline h22 h23 h24)
	(inline h24 h23 h22)
)
(:goal (and 
	(empty h0)
	(empty h1)
	(empty h2)
	(empty h3)
	(empty h4)
	(empty h5)
	(empty h6)
	(empty h7)
	(empty h9)
	(empty h10)
	(empty h11)
	(empty h12)
	(empty h13)
	(empty h14)
	(empty h15)
	(empty h16)
	(empty h17)
	(empty h18)
	(empty h19)
	(empty h20)
	(empty h21)
	(empty h22)
	(empty h23)
	(empty h24)
)))
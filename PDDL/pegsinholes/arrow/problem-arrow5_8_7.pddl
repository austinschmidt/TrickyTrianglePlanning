(define (problem arrow5_8_7)
(:domain pegs)
(:objects 
	p0 h0 p1 h1 p2 h2 p3 h3 p4 h4 p5 h5 p6 h6 p7 h7 p8 h8 p9 h9 
	p10 h10 p11 h11 p12 h12 p13 h13 p14 h14 p15 h15 p16 h16 p17 h17 p18 h18 p19 h19 
	p20 h20 p21 h21 p22 h22 p23 h23 p24 h24 p25 h25 p26 h26 p27 h27 p28 h28 p29 h29 
	p30 h30 p31 h31 p32 h32 p33 h33 p34 h34 p35 h35 p36 h36 p37 h37 p38 h38 p39 h39 
	p40 h40 p41 h41 p42 h42 p43 h43 p44 h44 p45 h45 p46 h46 p47 h47 p48 h48 p49 h49 
	p50 h50 p51 h51 h52 )
(:init
	(empty h8)
	(in p0 h0)
	(in p1 h1)
	(in p2 h2)
	(in p3 h3)
	(in p4 h4)
	(in p5 h5)
	(in p6 h6)
	(in p7 h7)
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
	(in p24 h25)
	(in p25 h26)
	(in p26 h27)
	(in p27 h28)
	(in p28 h29)
	(in p29 h30)
	(in p30 h31)
	(in p31 h32)
	(in p32 h33)
	(in p33 h34)
	(in p34 h35)
	(in p35 h36)
	(in p36 h37)
	(in p37 h38)
	(in p38 h39)
	(in p39 h40)
	(in p40 h41)
	(in p41 h42)
	(in p42 h43)
	(in p43 h44)
	(in p44 h45)
	(in p45 h46)
	(in p46 h47)
	(in p47 h48)
	(in p48 h49)
	(in p49 h50)
	(in p50 h51)
	(in p51 h52)
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
	(adjacent h20 h26)
	(adjacent h26 h20)
	(adjacent h21 h22)
	(adjacent h22 h21)
	(adjacent h21 h27)
	(adjacent h27 h21)
	(adjacent h22 h23)
	(adjacent h23 h22)
	(adjacent h22 h28)
	(adjacent h28 h22)
	(adjacent h23 h24)
	(adjacent h24 h23)
	(adjacent h23 h29)
	(adjacent h29 h23)
	(adjacent h24 h30)
	(adjacent h30 h24)
	(adjacent h25 h26)
	(adjacent h26 h25)
	(adjacent h25 h32)
	(adjacent h32 h25)
	(adjacent h26 h27)
	(adjacent h27 h26)
	(adjacent h26 h32)
	(adjacent h32 h26)
	(adjacent h26 h33)
	(adjacent h33 h26)
	(adjacent h27 h28)
	(adjacent h28 h27)
	(adjacent h27 h33)
	(adjacent h33 h27)
	(adjacent h27 h34)
	(adjacent h34 h27)
	(adjacent h28 h29)
	(adjacent h29 h28)
	(adjacent h28 h34)
	(adjacent h34 h28)
	(adjacent h28 h35)
	(adjacent h35 h28)
	(adjacent h29 h30)
	(adjacent h30 h29)
	(adjacent h29 h35)
	(adjacent h35 h29)
	(adjacent h29 h36)
	(adjacent h36 h29)
	(adjacent h30 h31)
	(adjacent h31 h30)
	(adjacent h30 h36)
	(adjacent h36 h30)
	(adjacent h30 h37)
	(adjacent h37 h30)
	(adjacent h31 h37)
	(adjacent h37 h31)
	(adjacent h32 h33)
	(adjacent h33 h32)
	(adjacent h32 h38)
	(adjacent h38 h32)
	(adjacent h33 h34)
	(adjacent h34 h33)
	(adjacent h33 h38)
	(adjacent h38 h33)
	(adjacent h33 h39)
	(adjacent h39 h33)
	(adjacent h34 h35)
	(adjacent h35 h34)
	(adjacent h34 h39)
	(adjacent h39 h34)
	(adjacent h34 h40)
	(adjacent h40 h34)
	(adjacent h35 h36)
	(adjacent h36 h35)
	(adjacent h35 h40)
	(adjacent h40 h35)
	(adjacent h35 h41)
	(adjacent h41 h35)
	(adjacent h36 h37)
	(adjacent h37 h36)
	(adjacent h36 h41)
	(adjacent h41 h36)
	(adjacent h36 h42)
	(adjacent h42 h36)
	(adjacent h37 h42)
	(adjacent h42 h37)
	(adjacent h38 h39)
	(adjacent h39 h38)
	(adjacent h38 h43)
	(adjacent h43 h38)
	(adjacent h39 h40)
	(adjacent h40 h39)
	(adjacent h39 h43)
	(adjacent h43 h39)
	(adjacent h39 h44)
	(adjacent h44 h39)
	(adjacent h40 h41)
	(adjacent h41 h40)
	(adjacent h40 h44)
	(adjacent h44 h40)
	(adjacent h40 h45)
	(adjacent h45 h40)
	(adjacent h41 h42)
	(adjacent h42 h41)
	(adjacent h41 h45)
	(adjacent h45 h41)
	(adjacent h41 h46)
	(adjacent h46 h41)
	(adjacent h42 h46)
	(adjacent h46 h42)
	(adjacent h43 h44)
	(adjacent h44 h43)
	(adjacent h43 h47)
	(adjacent h47 h43)
	(adjacent h44 h45)
	(adjacent h45 h44)
	(adjacent h44 h47)
	(adjacent h47 h44)
	(adjacent h44 h48)
	(adjacent h48 h44)
	(adjacent h45 h46)
	(adjacent h46 h45)
	(adjacent h45 h48)
	(adjacent h48 h45)
	(adjacent h45 h49)
	(adjacent h49 h45)
	(adjacent h46 h49)
	(adjacent h49 h46)
	(adjacent h47 h48)
	(adjacent h48 h47)
	(adjacent h47 h50)
	(adjacent h50 h47)
	(adjacent h48 h49)
	(adjacent h49 h48)
	(adjacent h48 h50)
	(adjacent h50 h48)
	(adjacent h48 h51)
	(adjacent h51 h48)
	(adjacent h49 h51)
	(adjacent h51 h49)
	(adjacent h50 h51)
	(adjacent h51 h50)
	(adjacent h50 h52)
	(adjacent h52 h50)
	(adjacent h51 h52)
	(adjacent h52 h51)
	(inline h0 h1 h2)
	(inline h2 h1 h0)
	(inline h0 h5 h10)
	(inline h10 h5 h0)
	(inline h0 h5 h11)
	(inline h11 h5 h0)
	(inline h1 h2 h3)
	(inline h3 h2 h1)
	(inline h1 h6 h11)
	(inline h11 h6 h1)
	(inline h1 h6 h12)
	(inline h12 h6 h1)
	(inline h2 h3 h4)
	(inline h4 h3 h2)
	(inline h2 h7 h12)
	(inline h12 h7 h2)
	(inline h2 h7 h13)
	(inline h13 h7 h2)
	(inline h3 h8 h13)
	(inline h13 h8 h3)
	(inline h3 h8 h14)
	(inline h14 h8 h3)
	(inline h4 h9 h14)
	(inline h14 h9 h4)
	(inline h4 h9 h15)
	(inline h15 h9 h4)
	(inline h5 h6 h7)
	(inline h7 h6 h5)
	(inline h5 h10 h15)
	(inline h15 h10 h5)
	(inline h5 h10 h16)
	(inline h16 h10 h5)
	(inline h6 h7 h8)
	(inline h8 h7 h6)
	(inline h6 h11 h16)
	(inline h16 h11 h6)
	(inline h6 h11 h17)
	(inline h17 h11 h6)
	(inline h7 h8 h9)
	(inline h9 h8 h7)
	(inline h7 h12 h17)
	(inline h17 h12 h7)
	(inline h7 h12 h18)
	(inline h18 h12 h7)
	(inline h8 h13 h18)
	(inline h18 h13 h8)
	(inline h8 h13 h19)
	(inline h19 h13 h8)
	(inline h9 h14 h19)
	(inline h19 h14 h9)
	(inline h9 h14 h20)
	(inline h20 h14 h9)
	(inline h10 h11 h12)
	(inline h12 h11 h10)
	(inline h10 h15 h20)
	(inline h20 h15 h10)
	(inline h10 h15 h21)
	(inline h21 h15 h10)
	(inline h11 h12 h13)
	(inline h13 h12 h11)
	(inline h11 h16 h21)
	(inline h21 h16 h11)
	(inline h11 h16 h22)
	(inline h22 h16 h11)
	(inline h12 h13 h14)
	(inline h14 h13 h12)
	(inline h12 h17 h22)
	(inline h22 h17 h12)
	(inline h12 h17 h23)
	(inline h23 h17 h12)
	(inline h13 h18 h23)
	(inline h23 h18 h13)
	(inline h13 h18 h24)
	(inline h24 h18 h13)
	(inline h14 h19 h24)
	(inline h24 h19 h14)
	(inline h14 h19 h25)
	(inline h25 h19 h14)
	(inline h15 h16 h17)
	(inline h17 h16 h15)
	(inline h15 h20 h26)
	(inline h26 h20 h15)
	(inline h16 h17 h18)
	(inline h18 h17 h16)
	(inline h16 h21 h27)
	(inline h27 h21 h16)
	(inline h17 h18 h19)
	(inline h19 h18 h17)
	(inline h17 h22 h28)
	(inline h28 h22 h17)
	(inline h18 h23 h29)
	(inline h29 h23 h18)
	(inline h19 h24 h30)
	(inline h30 h24 h19)
	(inline h20 h21 h22)
	(inline h22 h21 h20)
	(inline h21 h22 h23)
	(inline h23 h22 h21)
	(inline h22 h23 h24)
	(inline h24 h23 h22)
	(inline h25 h26 h27)
	(inline h27 h26 h25)
	(inline h25 h32 h38)
	(inline h38 h32 h25)
	(inline h26 h27 h28)
	(inline h28 h27 h26)
	(inline h26 h33 h39)
	(inline h39 h33 h26)
	(inline h27 h28 h29)
	(inline h29 h28 h27)
	(inline h27 h33 h38)
	(inline h38 h33 h27)
	(inline h27 h34 h40)
	(inline h40 h34 h27)
	(inline h28 h29 h30)
	(inline h30 h29 h28)
	(inline h28 h34 h39)
	(inline h39 h34 h28)
	(inline h28 h35 h41)
	(inline h41 h35 h28)
	(inline h29 h30 h31)
	(inline h31 h30 h29)
	(inline h29 h35 h40)
	(inline h40 h35 h29)
	(inline h29 h36 h42)
	(inline h42 h36 h29)
	(inline h30 h36 h41)
	(inline h41 h36 h30)
	(inline h31 h37 h42)
	(inline h42 h37 h31)
	(inline h32 h33 h34)
	(inline h34 h33 h32)
	(inline h32 h38 h43)
	(inline h43 h38 h32)
	(inline h33 h34 h35)
	(inline h35 h34 h33)
	(inline h33 h39 h44)
	(inline h44 h39 h33)
	(inline h34 h35 h36)
	(inline h36 h35 h34)
	(inline h34 h39 h43)
	(inline h43 h39 h34)
	(inline h34 h40 h45)
	(inline h45 h40 h34)
	(inline h35 h36 h37)
	(inline h37 h36 h35)
	(inline h35 h40 h44)
	(inline h44 h40 h35)
	(inline h35 h41 h46)
	(inline h46 h41 h35)
	(inline h36 h41 h45)
	(inline h45 h41 h36)
	(inline h37 h42 h46)
	(inline h46 h42 h37)
	(inline h38 h39 h40)
	(inline h40 h39 h38)
	(inline h38 h43 h47)
	(inline h47 h43 h38)
	(inline h39 h40 h41)
	(inline h41 h40 h39)
	(inline h39 h44 h48)
	(inline h48 h44 h39)
	(inline h40 h41 h42)
	(inline h42 h41 h40)
	(inline h40 h44 h47)
	(inline h47 h44 h40)
	(inline h40 h45 h49)
	(inline h49 h45 h40)
	(inline h41 h45 h48)
	(inline h48 h45 h41)
	(inline h42 h46 h49)
	(inline h49 h46 h42)
	(inline h43 h44 h45)
	(inline h45 h44 h43)
	(inline h43 h47 h50)
	(inline h50 h47 h43)
	(inline h44 h45 h46)
	(inline h46 h45 h44)
	(inline h44 h48 h51)
	(inline h51 h48 h44)
	(inline h45 h48 h50)
	(inline h50 h48 h45)
	(inline h46 h49 h51)
	(inline h51 h49 h46)
	(inline h47 h48 h49)
	(inline h49 h48 h47)
	(inline h47 h50 h52)
	(inline h52 h50 h47)
	(inline h49 h51 h52)
	(inline h52 h51 h49)
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
	(empty h25)
	(empty h26)
	(empty h27)
	(empty h28)
	(empty h29)
	(empty h30)
	(empty h31)
	(empty h32)
	(empty h33)
	(empty h34)
	(empty h35)
	(empty h36)
	(empty h37)
	(empty h38)
	(empty h39)
	(empty h40)
	(empty h41)
	(empty h42)
	(empty h43)
	(empty h44)
	(empty h45)
	(empty h46)
	(empty h47)
	(empty h48)
	(empty h49)
	(empty h50)
	(empty h51)
	(empty h52)
)))
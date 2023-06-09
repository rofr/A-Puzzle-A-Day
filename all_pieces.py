
#pieces -> set of all pieces and possible moves
#board -> array of size 43 (12 + 31) 0-11 is months, 12-42 is days
# to solve for a 


def all_pieces():
   return [
      [
        # 000
        # 000
        [0,1,2,6,7,8],
        [1,2,3,7,8,9],
        [2,3,4,8,9,10],
        [3,4,5,9,10,11],
        [6,7,8,12,13,14],
        [7,8,9,13,14,15],
        [8,9,10,14,15,16],
        [9,10,11,15,16,17],
        [12,13,14,19,20,21],
        [13,14,15,20,21,22],
        [14,15,16,21,22,23],
        [15,16,17,22,23,24],
        [16,17,18,23,24,25],
        [19,20,21,26,27,28],
        [20,21,22,27,28,29],
        [21,22,23,28,29,30],
        [22,23,24,29,30,31],
        [23,24,25,30,31,32],
        #[26,27,28,33,34,35],
        [27,28,29,34,35,36],
        [28,29,30,35,36,37],
        [29,30,31,36,37,38],
        [30,31,32,37,38,39],
        [33,34,35,40,41,42],
        # vertical orientation
        # 00
        # 00
        # 00
        [0,1,6,7,12,13],
        [1,2,7,8,13,14],
        [2,3,8,9,14,15],
        [3,4,9,10,15,16],
        [4,5,10,11,16,17],
        [6,7,12,13,19,20],
        [7,8,13,14,20,21],
        [8,9,14,15,21,22],
        [9,10,15,16,22,23],
        [10,11,16,17,23,24],
        [12,13,19,20,26,27],
        [13,14,20,21,27,28],
        [14,15,21,22,28,29],
        [15,16,22,23,29,30],
        [16,17,23,24,30,31],
        [17,18,24,25,31,32],
        [19,20,26,27,33,34],
        [20,21,27,28,34,35],
        [21,22,28,29,35,36],
        [22,23,29,30,36,37],
        [23,24,30,31,37,38],
        [24,25,31,32,38,39],
        [26,27,33,34,40,41],
        [27,28,34,35,41,42]
      ],
      # yellow 
      [
        # 000
        # 00
        [0,1,2,6,7],
        [1,2,3,7,8],
        [2,3,4,8,9],
        [3,4,5,9,10],
        [6,7,8,12,13],
        [7,8,9,13,14],
        [8,9,10,14,15],
        [9,10,11,15,16],
        [12,13,14,19,20],
        [13,14,15,20,21],
        [14,15,16,21,22],
        [15,16,17,22,23],
        [16,17,18,23,24],
        [19,20,21,26,27],
        [20,21,22,27,28],
        [21,22,23,28,29],
        [22,23,24,29,30],
        [23,24,25,30,31],
        [26,27,28,33,34],
        [27,28,29,34,35],
        [28,29,30,35,36],
        [29,30,31,36,37],
        [30,31,32,37,38],
        [33,34,35,40,41],
        [34,35,36,41,42],
        # 00
        # 000
        [0,1,6,7,8],
        [1,2,7,8,9],
        [2,3,8,9,10],
        [3,4,9,10,11],
        [6,7,12,13,14],
        [7,8,13,14,15],
        [8,9,14,15,16],
        [9,10,15,16,17],
        [10,11,16,17,18],
        [12,13,19,20,21],
        [13,14,20,21,22],
        [14,15,21,22,23],
        [15,16,22,23,24],
        [16,17,23,24,25],
        [19,20,26,27,28],
        [20,21,27,28,29],
        [21,22,28,29,30],
        [22,23,29,30,31],
        [23,24,30,31,32],
        #[26,27,33,34,35],
        [27,28,34,35,36],
        [28,29,35,36,37],
        [29,30,36,37,38],
        [30,31,37,38,39],
        [33,34,40,41,42],
        #  00
        # 000
        [1,2,6,7,8],
        [2,3,7,8,9],
        [3,4,8,9,10],
        [4,5,9,10,11],
        [7,8,12,13,14],
        [8,9,13,14,15],
        [9,10,14,15,16],
        [10,11,15,16,17],
        [13,14,19,20,21],
        [14,15,20,21,22],
        [15,16,21,22,23],
        [16,17,22,23,24],
        [17,18,23,24,25],
        [20,21,26,27,28],
        [21,22,27,28,29],
        [22,23,28,29,30],
        [23,24,29,30,31],
        [24,25,30,31,32],
        #[27,28,33,34,35],
        [28,29,34,35,36],
        [29,30,35,36,37],
        [30,31,36,37,38],
        [31,32,37,38,39],
        [34,35,40,41,42],
        # 000
        #  00
        [0,1,2,7,8],
        [1,2,3,8,9],
        [2,3,4,9,10],
        [3,4,5,10,11],
        [6,7,8,13,14],
        [7,8,9,14,15],
        [8,9,10,15,16],
        [9,10,11,16,17],
        [12,13,14,20,21],
        [13,14,15,21,22],
        [14,15,16,22,23],
        [15,16,17,23,24],
        [16,17,18,24,25],
        [19,20,21,27,28],
        [20,21,22,28,29],
        [21,22,23,29,30],
        [22,23,24,30,31],
        [23,24,25,31,32],
        #[26,27,28,34,35],
        #[27,28,29,35,36],
        [28,29,30,36,37],
        [29,30,31,37,38],
        [30,31,32,38,39],
        [33,34,35,41,42],
        # 0
        # 00
        # 00
        [0,6,7,12,13],
        [1,7,8,13,14],
        [2,8,9,14,15],
        [3,9,10,15,16],
        [4,10,11,16,17],
        [6,12,13,19,20],
        [7,13,14,20,21],
        [8,14,15,21,22],
        [9,15,16,22,23],
        [10,16,17,23,24],
        [11,17,18,24,25],
        [12,19,20,26,27],
        [13,20,21,27,28],
        [14,21,22,28,29],
        [15,22,23,29,30],
        [16,23,24,30,31],
        [17,24,25,31,32],
        [19,26,27,33,34],
        [20,27,28,34,35],
        [21,28,29,35,36],
        [22,29,30,36,37],
        [23,30,31,37,38],
        [24,31,32,38,39],
        [26,33,34,40,41],
        [27,34,35,41,42],
        #  0
        # 00
        # 00
        [1,6,7,12,13],
        [2,7,8,13,14],
        [3,8,9,14,15],
        [4,9,10,15,16],
        [5,10,11,16,17],
        [7,12,13,19,20],
        [8,13,14,20,21],
        [9,14,15,21,22],
        [10,15,16,22,23],
        [11,16,17,23,24],
        [13,19,20,26,27],
        [14,20,21,27,28],
        [15,21,22,28,29],
        [16,22,23,29,30],
        [17,23,24,30,31],
        [18,24,25,31,32],
        [20,26,27,33,34],
        [21,27,28,34,35],
        [22,28,29,35,36],
        [23,29,30,36,37],
        [24,30,31,37,38],
        [25,31,32,38,39],
        [27,33,34,40,41],
        [28,34,35,41,42],        
        # 00
        # 00
        # 0
        [0,1,6,7,12],
        [1,2,7,8,13],
        [2,3,8,9,14],
        [3,4,9,10,15],
        [4,5,10,11,16],
        [6,7,12,13,19],
        [7,8,13,14,20],
        [8,9,14,15,21],
        [9,10,15,16,22],
        [10,11,16,17,23],
        [12,13,19,20,26],
        [13,14,20,21,27],
        [14,15,21,22,28],
        [15,16,22,23,29],
        [16,17,23,24,30],
        [17,18,24,25,31],
        [19,20,26,27,33],
        [20,21,27,28,34],
        [21,22,28,29,35],
        [22,23,29,30,36],
        [23,24,30,31,37],
        [24,25,31,32,38],
        [26,27,33,34,40],
        [27,28,34,35,41],
        # 00
        # 00
        #  0
        [0,1,6,7,13],
        [1,2,7,8,14],
        [2,3,8,9,15],
        [3,4,9,10,16],
        [4,5,10,11,17],
        [6,7,12,13,20],
        [7,8,13,14,21],
        [8,9,14,15,22],
        [9,10,15,16,23],
        [10,11,16,17,24],
        [12,13,19,20,27],
        [13,14,20,21,28],
        [14,15,21,22,29],
        [15,16,22,23,30],
        [16,17,23,24,31],
        [17,18,24,25,32],
        [19,20,26,27,34],
        [20,21,27,28,35],
        [21,22,28,29,36],
        [22,23,29,30,37],
        [23,24,30,31,38],
        [24,25,31,32,39],
        [26,27,33,34,41],
        [27,28,34,35,42],
      ],
      [
        # 000
        # 0 0
        [0,1,2,6,8],
        [1,2,3,7,9],
        [2,3,4,8,10],
        [3,4,5,9,11],
        [6,7,8,12,14],
        [7,8,9,13,15],
        [8,9,10,14,16],
        [9,10,11,15,17],
        [12,13,14,19,21],
        [13,14,15,20,22],
        [14,15,16,21,23],
        [15,16,17,22,24],
        [16,17,18,23,25],
        [19,20,21,26,28],
        [20,21,22,27,29],
        [21,22,23,28,30],
        [22,23,24,29,31],
        [23,24,25,30,32],
        #[26,27,28,33,35],
        [27,28,29,34,36],
        [28,29,30,35,37],
        [29,30,31,36,38],
        [30,31,32,37,39],
        [33,34,35,40,42],

        # 0 0
        # 000
        [0,2,6,7,8],
        [1,3,7,8,9],
        [2,4,8,9,10],
        [3,5,9,10,11],
        [6,8,12,13,14],
        [7,9,13,14,15],
        [8,10,14,15,16],
        [9,11,15,16,17],
        [12,14,19,20,21],
        [13,15,20,21,22],
        [14,16,21,22,23],
        [15,17,22,23,24],
        [16,18,23,24,25],
        [19,21,26,27,28],
        [20,22,27,28,29],
        [21,23,28,29,30],
        [22,24,29,30,31],
        [23,25,30,31,32],
        #[26,28,33,34,35],
        [27,29,34,35,36],
        [28,30,35,36,37],
        [29,31,36,37,38],
        [30,32,37,38,39],
        [33,35,40,41,42],               
        # 00
        # 0
        # 00
        [0,1,6,12,13],
        [1,2,7,13,14],
        [2,3,8,14,15],
        [3,4,9,15,16],
        [4,5,10,16,17],
        [6,7,12,19,20],
        [7,8,13,20,21],
        [8,9,14,21,22],
        [9,10,15,22,23],
        [10,11,16,23,24],
        [12,13,19,26,27],
        [13,14,20,27,28],
        [14,15,21,28,29],
        [15,16,22,29,30],
        [16,17,23,30,31],
        [17,18,24,31,32],
        [19,20,26,33,34],
        [20,21,27,34,35],
        [21,22,28,35,36],
        [22,23,29,36,37],
        [23,24,30,37,38],
        [24,25,31,38,39],
        [26,27,33,40,41],
        [27,28,34,41,42],
         # 00
         #  0
         # 00
        [0,1,7,12,13],
        [1,2,8,13,14],
        [2,3,9,14,15],
        [3,4,10,15,16],
        [4,5,11,16,17],
        [6,7,13,19,20],
        [7,8,14,20,21],
        [8,9,15,21,22],
        [9,10,16,22,23],
        [10,11,17,23,24],
        [12,13,20,26,27],
        [13,14,21,27,28],
        [14,15,22,28,29],
        [15,16,23,29,30],
        [16,17,24,30,31],
        [17,18,25,31,32],
        [19,20,27,33,34],
        [20,21,28,34,35],
        [21,22,29,35,36],
        [22,23,30,36,37],
        [23,24,31,37,38],
        [24,25,32,38,39],
        [26,27,34,40,41],
        [27,28,35,41,42]
      ],
      [
        # 0
        # 0000
        [0,6,7,8,9],
        [1,7,8,9,10],
        #[2,8,9,10,11],
        [6,12,13,14,15],
        [7,13,14,15,16],
        [8,14,15,16,17],
        [9,15,16,17,18],
        [12,19,20,21,22],
        [13,20,21,22,23],
        [14,21,22,23,24],
        [15,22,23,24,25],
        [19,26,27,28,29],
        [20,27,28,29,30],
        [21,28,29,30,31],
        [22,29,30,31,32],
        #[26,33,34,35,36],
        [27,34,35,36,37],
        [28,35,36,37,38],
        [29,36,37,38,39],

        # 0000
        # 0
        [0,1,2,3,6],
        [1,2,3,4,7],
        [2,3,4,5,8],
        [6,7,8,9,12],
        [7,8,9,10,13],
        [8,9,10,11,14],
        [12,13,14,15,19],
        [13,14,15,16,20],
        [14,15,16,17,21],
        [15,16,17,18,22],
        [19,20,21,22,26],
        [20,21,22,23,27],
        [21,22,23,24,28],
        [22,23,24,25,29],
        [26,27,28,29,33],
        [27,28,29,30,34],
        [28,29,30,31,35],
        [29,30,31,32,36],
        [33,34,35,36,40],
        [34,35,36,37,41],
        [35,36,37,38,42],

        # 0000
        #    0
        [0,1,2,3,9],
        [1,2,3,4,10],
        [2,3,4,5,11],
        [6,7,8,9,15],
        [7,8,9,10,16],
        [8,9,10,11,17],
        [12,13,14,15,22],
        [13,14,15,16,23],
        [14,15,16,17,24],
        [15,16,17,18,25],
        [19,20,21,22,29],
        [20,21,22,23,30],
        [21,22,23,24,31],
        [22,23,24,25,32],
        [26,27,28,29,36],
        [27,28,29,30,37],
        [28,29,30,31,38],
        [29,30,31,32,39],

        #    0
        # 0000
        #[3,6,7,8,9],
        [4,7,8,9,10],
        [5,8,9,10,11],
        [9,12,13,14,15],
        [10,13,14,15,16],
        [11,14,15,16,17],
        [15,19,20,21,22],
        [16,20,21,22,23],
        [17,21,22,23,24],
        [18,22,23,24,25],
        [22,26,27,28,29],
        [23,27,28,29,30],
        [24,28,29,30,31],
        #[25,29,30,31,32],
        #[29,33,34,35,36],
        [30,34,35,36,37],
        [31,35,36,37,38],
        [32,36,37,38,39],
        
        # 00
        # 0
        # 0
        # 0
        [0,1,6,12,19],
        [1,2,7,13,20],
        [2,3,8,14,21],
        [3,4,9,15,22],
        [4,5,10,16,23],
        [6,7,12,19,26],
        [7,8,13,20,27],
        [8,9,14,21,28],
        [9,10,15,22,29],
        [10,11,16,23,30],
        [12,13,19,26,33],
        [13,14,20,27,34],
        [14,15,21,28,35],
        [15,16,22,29,36],
        [16,17,23,30,37],
        #[17,18,24,31,38],
        [19,20,26,33,40],
        #[20,21,27,34,41],
        [21,22,28,35,42],

        # 00
        #  0
        #  0
        #  0
        [0,1,7,13,20],
        [1,2,8,14,21],
        [2,3,9,15,22],
        [3,4,10,16,23],
        [4,5,11,17,24],
        [6,7,13,20,27],
        [7,8,14,21,28],
        [8,9,15,22,29],
        [9,10,16,23,30],
        [10,11,17,24,31],
        [12,13,20,27,34],
        [13,14,21,28,35],
        [14,15,22,29,36],
        [15,16,23,30,37],
        #[16,17,24,31,38],
        [17,18,25,32,39],
        #[19,20,27,34,41],
        [20,21,28,35,42],

        # 0
        # 0
        # 0
        # 00
        [0,6,12,19,20],
        [1,7,13,20,21],
        [2,8,14,21,22],
        [3,9,15,22,23],
        [4,10,16,23,24],
        [5,11,17,24,25],
        [6,12,19,26,27],
        [7,13,20,27,28],
        [8,14,21,28,29],
        [9,15,22,29,30],
        [10,16,23,30,31],
        #[11,17,24,31,32],
        [12,19,26,33,34],
        [13,20,27,34,35],
        [14,21,28,35,36],
        [15,22,29,36,37],
        [16,23,30,37,38],
        #[17,24,31,38,39],
        [19,26,33,40,41],
        #[20,27,34,41,42],
        #  0
        #  0
        #  0
        # 00
        #[1,7,13,19,20],
        [2,8,14,20,21],
        [3,9,15,21,22],
        [4,10,16,22,23],
        [5,11,17,23,24],
        [7,13,20,26,27],
        [8,14,21,27,28],
        [9,15,22,28,29],
        [10,16,23,29,30],
        [11,17,24,30,31],
        [13,20,27,33,34],
        [14,21,28,34,35],
        [15,22,29,35,36],
        [16,23,30,36,37],
        #[17,24,31,37,38],
        [18,25,32,38,39],
        [20,27,34,40,41],
        [21,28,35,41,42],
      ],
      [
        #  0
        # 0000
        [1,6,7,8,9],
        [2,7,8,9,10],
        #[3,8,9,10,11],
        [7,12,13,14,15],
        [8,13,14,15,16],
        [9,14,15,16,17],
        [10,15,16,17,18],
        [13,19,20,21,22],
        [14,20,21,22,23],
        [15,21,22,23,24],
        [16,22,23,24,25],
        [20,26,27,28,29],
        [21,27,28,29,30],
        [22,28,29,30,31],
        [23,29,30,31,32],
        #[27],
        [28,34,35,36,37],
        [29,35,36,37,38],
        [30,36,37,38,39],

        #   0
        # 0000
        #[2,6,7,8,9],
        [3,7,8,9,10],
        [4,8,9,10,11],
        [8,12,13,14,15],
        [9,13,14,15,16],
        [10,14,15,16,17],
        [11,15,16,17,18],
        [14,19,20,21,22],
        [15,20,21,22,23],
        [16,21,22,23,24],
        [17,22,23,24,25],
        [21,26,27,28,29],
        [22,27,28,29,30],
        [23,28,29,30,31],
        [24,29,30,31,32],
        #[28],
        [29,34,35,36,37],
        [30,35,36,37,38],
        [31,36,37,38,39],
     
         # 0000
         #  0
         [0,1,2,3,7],
         [1,2,3,4,8],
         [2,3,4,5,9],
         [6,7,8,9,13],
         [7,8,9,10,14],
         [8,9,10,11,15],
         [12,13,14,15,20],
         [13,14,15,16,21],
         [14,15,16,17,22],
         [15,16,17,18,23],
         [19,20,21,22,27],
         [20,21,22,23,28],
         [21,22,23,24,29],
         [22,23,24,25,30],
         [26,27,28,29,34],
         [27,28,29,30,35],
         [28,29,30,31,36],
         #[29],
         [34,35,36,37,42],

        # 0000
        #   0
         [0,1,2,3,8],
         [1,2,3,4,9],
         [2,3,4,5,10],
         [6,7,8,9,14],
         [7,8,9,10,15],
         [8,9,10,11,16],
         [12,13,14,15,21],
         [13,14,15,16,22],
         [14,15,16,17,23],
         [15,16,17,18,24],
         [19,20,21,22,28],
         [20,21,22,23,29],
         [21,22,23,24,30],
         [22,23,24,25,31],
         [26,27,28,29,35],
         [27,28,29,30,36],
         [28,29,30,31,37],
         [29,30,31,32,38],
         #[33,34,35,36,42],
         # 0
         # 00
         # 0
         # 0
         [0,6,7,12,19],
         [1,7,8,13,20],
         [2,8,9,14,21],
         [3,9,10,15,22],
         [4,10,11,16,23],
         [6,12,13,19,26],
         [7,13,14,20,27],
         [8,14,15,21,28],
         [9,15,16,22,29],
         [10,16,17,23,30],
         [11,17,18,24,31],
         [12,19,20,26,33],
         [13,20,21,27,34],
         [14,21,22,28,35],
         [15,22,23,29,36],
         [16,23,24,30,37],
         #[17,24,25,31,38],
         [19,26,27,33,40],
         [20,27,28,34,41],
         [21,28,29,35,42],

         # 0
         # 0
         # 00
         # 0
         [0,6,12,13,19],
         [1,7,13,14,20],
         [2,8,14,15,21],
         [3,9,15,16,22],
         #[4,10,16,17,23],
         [5,11,17,18,24],
         [6,12,19,20,26],
         [7,13,20,21,27],
         [8,14,21,22,28],
         [9,15,22,23,29],
         [10,16,23,24,30],
         [11,17,24,25,31],
         [12,19,26,27,33],
         [13,20,27,28,34],
         [14,21,28,29,35],
         [15,22,29,30,36],
         [16,23,30,31,37],
         #[17,24,31,32,38],
         [19,26,33,34,40],
         #[20,27,34,35,41],
         [21,28,35,36,42],        
         #  0
         # 00
         #  0
         #  0
         [1,6,7,13,20],
         [2,7,8,14,21],
         [3,8,9,15,22],
         [4,9,10,16,23],
         [5,10,11,17,24],
         [7,12,13,20,27],
         [8,13,14,21,28],
         [9,14,15,22,29],
         [10,15,16,23,30],
         [11,16,17,24,31],
         [13,19,20,27,34],
         [14,20,21,28,35],
         [15,21,22,29,36],
         [16,22,23,30,37],
         #[17,23,24,31,38],
         [18,24,25,32,39],
         #[20,26,27,34,41],
         [21,27,28,35,42],

         #  0
         #  0
         # 00
         #  0
         [1,7,12,13,20],
         [2,8,13,14,21],
         [3,9,14,15,22],
         [4,10,15,16,23],
         [5,11,16,17,24],
         [7,13,19,20,27],
         [8,14,20,21,28],
         [9,15,21,22,29],
         [10,16,22,23,30],
         [11,17,23,24,31],
         [13,20,26,27,34],
         [14,21,27,28,35],
         [15,22,28,29,36],
         [16,23,29,30,37],
         #[17,24,30,31,38],
         [18,25,31,32,39],
         [20,27,33,34,41],
         [21,28,34,35,42]
      ],
      [
        # 000
        # 0
        # 0
        [0,1,2,6,12],
        [1,2,3,7,13],
        [2,3,4,8,14],
        [3,4,5,9,15],
        [6,7,8,12,19],
        [7,8,9,13,20],
        [8,9,10,14,21],
        [9,10,11,15,22],
        [12,13,14,19,26],
        [13,14,15,20,27],
        [14,15,16,21,28],
        [15,16,17,22,29],
        [16,17,18,23,30],
        [19,20,21,26,33],
        [20,21,22,27,34],
        [21,22,23,28,35],
        [22,23,24,29,36],
        #[23,24,25,30,37],
        [26,27,28,33,40],
        [27,28,29,34,41],
        [28,29,30,35,42],
        # 000
        #   0
        #   0
        [0,1,2,8,14],
        [1,2,3,9,15],
        [2,3,4,10,16],
        [3,4,5,11,17],
        [6,7,8,14,21],
        [7,8,9,15,22],
        [8,9,10,16,23],
        [9,10,11,17,24],
        [12,13,14,21,28],
        [13,14,15,22,29],
        [14,15,16,23,30],
        [15,16,17,24,31],
        [16,17,18,25,32],
        [19,20,21,28,35],
        [20,21,22,29,36],
        [21,22,23,30,37],
        [22,23,24,31,38], #?
        [23,24,25,32,39],
        #[26,27,28,33,40],
        # 0
        # 0
        # 000
        [0,6,12,13,14],
        [1,7,13,14,15],
        [2,8,14,15,16],
        #[3,9,15,16,17],
        #[4,10,16,17,18],
        [6,12,19,20,21],
        [7,13,20,21,22],
        [8,14,21,22,23],
        [9,15,22,23,24],
        [10,16,23,24,25],
        [12,19,26,27,28],
        [13,20,27,28,29],
        [14,21,28,29,30],
        [15,22,29,30,31],
        [16,23,30,31,32],
        #[19],
        [20,27,34,35,36],
        [21,28,35,36,37],
        [22,29,36,37,38],
        [23,30,37,38,39],
        [26,33,40,41,42],
        #   0
        #   0
        # 000
        [2,8,12,13,14],
        [3,9,13,14,15],
        [4,10,14,15,16],
        [5,11,15,16,17],
        #[4,10,16,17,18],
        [8,14,19,20,21],
        [9,15,20,21,22],
        [10,16,21,22,23],
        [11,17,22,23,24],
        [14,21,26,27,28],
        [15,22,27,28,29],
        [16,23,28,29,30],
        [17,24,29,30,31],
        [18,25,30,31,32],
        #[21],
        [22,29,34,35,36],
        [23,30,35,36,37],
        [24,31,36,37,38],
        [25,32,37,38,39],
        [28,35,40,41,42],
      ],
      [
        # 000
        #   00
        [0,1,2,8,9],
        [1,2,3,9,10],
        [2,3,4,10,11],
        [6,7,8,14,15],
        [7,8,9,15,16],
        [8,9,10,16,17],
        [9,10,11,17,18],
        [12,13,14,21,22],
        [13,14,15,22,23],
        [14,15,16,23,24],
        [15,16,17,24,25],
        [19,20,21,28,29],
        [20,21,22,29,30],
        [21,22,23,30,31],
        [22,23,24,31,32],
        [26,27,28,35,36],
        [27,28,29,36,37],
        [28,29,30,37,38],
        [29,30,31,38,39],
        #   00
        # 000
        [2,3,6,7,8],
        [3,4,7,8,9],
        [4,5,8,9,10],
        [8,9,12,13,14],
        [9,10,13,14,15],
        [10,11,14,15,16],
        [14,15,19,20,21],
        [15,16,20,21,22],
        [16,17,21,22,23],
        [17,18,22,23,24],
        [21,22,26,27,28],
        [22,23,27,28,29],
        [23,24,28,29,30],
        [24,25,29,30,31],
        #[28],
        [29,30,34,35,36],
        [30,31,35,36,37],
        [31,32,36,37,38],
        [35,36,40,41,42],
        # 00
        #  000
        [0,1,7,8,9],
        [1,2,8,9,10],
        #[2,3,9,10,11],
        [6,7,13,14,15],
        [7,8,14,15,16],
        [8,9,15,16,17],
        [9,10,16,17,18],
        [12,13,20,21,22],
        [13,14,21,22,23],
        [14,15,22,23,24],
        [15,16,23,24,25],
        [19,20,27,28,29],
        [20,21,28,29,30],
        [21,22,29,30,31],
        [22,23,30,31,32],
        #[26,27,34,35,36],
        [27,28,35,36,37],
        [28,29,36,37,38],
        [29,30,37,38,39],

        #  000
        # 00
        [1,2,3,6,7],
        [2,3,4,7,8],
        [3,4,5,8,9],
        [7,8,9,12,13],
        [8,9,10,13,14],
        [9,10,11,14,15],
        [13,14,15,19,20],
        [14,15,16,20,21],
        [15,16,17,21,22],
        [16,17,18,22,23],
        [20,21,22,26,27],
        [21,22,23,27,28],
        [22,23,24,28,29],
        [23,24,25,29,30],
        [27,28,29,33,34],
        [28,29,30,34,35],
        [29,30,31,35,36],
        #[30,31,32,36,37],
        [34,35,36,40,41],
        [35,36,37,41,42],

        # 0
        # 00
        #  0
        #  0
        [0,6,7,13,20],
        [1,7,8,14,21],
        [2,8,9,15,22],
        [3,9,10,16,23],
        [4,10,11,17,24],
        [6,12,13,20,27],
        [7,13,14,21,28],
        [8,14,15,22,29],
        [9,15,16,23,30],
        [10,16,17,24,31],
        [11,17,18,25,32],
        [12,19,20,27,34],
        [13,20,21,28,35],
        [14,21,22,29,36],
        [15,22,23,30,37],
        #[16,23,24,31,38],
        [17,24,25,32,39],
        #[19],
        [20,27,28,35,42],

        #  0
        # 00
        # 0
        # 0
        [1,6,7,12,19],
        [2,7,8,13,20],
        [3,8,9,14,21],
        [4,9,10,15,22],
        [5,10,11,16,23],
        [7,12,13,19,26],
        [8,13,14,20,27],
        [9,14,15,21,28],
        [10,15,16,22,29],
        [11,16,17,23,30],
        [13,19,20,26,33],
        [14,20,21,27,34],
        [15,21,22,28,35],
        [16,22,23,29,36],
        [17,23,24,30,37],
        #[18,24,25,31,38],
        [20,26,27,33,40],
        [21,27,28,34,41],
        [22,28,29,35,42],
        # 0
        # 0
        # 00
        #  0
        [0,6,12,13,20],
        [1,7,13,14,21],
        [2,8,14,15,22],
        [3,9,15,16,23],
        #[4,10,16,17,24],
        [5,11,17,18,25],
        [6,12,19,20,27],
        [7,13,20,21,28],
        [8,14,21,22,29],
        [9,15,22,23,30],
        [10,16,23,24,31],
        [11,17,24,25,32],
        [12,19,26,27,34],
        [13,20,27,28,35],
        [14,21,28,29,36],
        [15,22,29,30,37],
        [16,23,30,31,38],
        #[17]
        [19,26,33,34,41],
        [20,27,34,35,42], #?

        #  0
        #  0
        # 00
        # 0
        [1,7,12,13,19],
        [2,8,13,14,20],
        [3,9,14,15,21],
        [4,10,15,16,22],
        [5,11,16,17,23],
        [7,13,19,20,26],
        [8,14,20,21,27],
        [9,15,21,22,28],
        [10,16,22,23,29],
        [11,17,23,24,30],
        [13,20,26,27,33],
        [14,21,27,28,34],
        [15,22,28,29,35],
        [16,23,29,30,36],
        #[17]
        [18,25,31,32,38],
        [20,27,33,34,40],
        [21,28,34,35,41],
        [22,29,35,36,42]
      ],
      [
        #  00
        #  0
        # 00
        #[1,2,7,12,13],
        [2,3,8,13,14],
        [3,4,9,14,15],
        [4,5,10,15,16],
        [7,8,13,19,20],
        [8,9,14,20,21],
        [9,10,15,21,22],
        [10,11,16,22,23],
        [13,14,20,26,27],
        [14,15,21,27,28],
        [15,16,22,28,29],
        [16,17,23,29,30],
        [17,18,24,30,31],
        [20,21,27,33,34],
        [21,22,28,34,35],
        [22,23,29,35,36],
        [23,24,30,36,37],
        #[24,25,31,37,38],
        [27,28,34,40,41],
        [28,29,35,41,42],
        # 00
        #  0
        #  00
        [0,1,7,13,14],
        [1,2,8,14,15],
        [2,3,9,15,16],
        #[3]
        [4,5,11,17,18],
        [6,7,13,20,21],
        [7,8,14,21,22],
        [8,9,15,22,23],
        [9,10,16,23,24],
        [10,11,17,24,25],
        [12,13,20,27,28],
        [13,14,21,28,29],
        [14,15,22,29,30],
        [15,16,23,30,31],
        #[16,17,24,31,32],
        [19,20,27,34,35],
        [20,21,28,35,36],
        [21,22,29,36,37],
        [22,23,30,37,38],
        [23,24,31,38,39],
        #   0
        # 000
        # 0
        [3,7,8,9,13],
        [4,8,9,10,14],
        [5,9,10,11,15],
        [8,12,13,14,19],
        [9,13,14,15,20],
        [10,14,15,16,21],
        [11,15,16,17,22],
        [14,19,20,21,26],
        [15,20,21,21,27],
        [16,21,22,23,28],
        [17,22,23,24,29],
        [18,23,24,25,30],
        [21,26,27,28,33],
        [22,27,28,29,34],
        [23,28,29,30,35],
        [24,29,30,31,36],
        #[25,30,31,32,37],
        #[28],
        [29,34,35,36,41],
        [30,35,36,37,42],
        # 0
        # 000
        #   0
        [0,6,7,8,14],
        [1,7,8,9,15],
        [2,8,9,10,16],
        #[3],
        [6,12,13,14,21],
        [7,13,14,15,22],
        [8,14,15,16,23],
        [9,15,16,17,24],
        [10,16,17,18,25],
        [12,19,20,21,28],
        [13,20,21,22,29],
        [14,21,22,23,30],
        [15,22,23,24,31],
        [16,23,24,25,32],
        [19,26,27,28,35],
        [20,27,28,29,36],
        [21,28,29,30,37],
        [22,29,30,31,38],
        [23,30,31,32,39]
      ]
]

class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                if (Character.isDigit(board[i][j])){
                    // checking horizontal
                    for (int k=j; k<9; k++){
                        if(board[i][j] == board[i][k] && k!=j){
                            return false;
                        }
                    }

                    // checking vertical
                    for (int k=i; k<9; k++){
                        if (board[i][j] == board[k][j] && k !=i){
                            return false;
                        }
                    }

                    // cheking 3*3
                    int quoVertical = ((int) i/3) * 3;
                    int quoHorizon = ((int) j/3) * 3;
                    for(int k=quoVertical;k<quoVertical+3;k++){
                        for(int m=quoHorizon; m<quoHorizon+3; m++){
                            if ((board[i][j] == board[k][m]) && (i != k) && (j != m)){
                                return false;
                            }
                        }
                    }
                }
            }
            }
        
        return true;
    }
}
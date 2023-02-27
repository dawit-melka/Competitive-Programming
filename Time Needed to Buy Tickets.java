class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int count = 0;
        for( int i = 0; i < tickets.length; i++){
            count += Math.min(tickets[k], tickets[i]);
            if (i > k && tickets[k] <= tickets[i])
                count -= 1;
        }
        return count;
    }
}

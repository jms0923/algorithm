package StringArray;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;


//Definition of Interval:
class Interval {
    int start, end;
    Interval(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

public class MeetiingRooms {

    public static void main(String[] args) {

        Interval in1 = new Interval(15,20);
        Interval in2 = new Interval(5,10);
        Interval in3 = new Interval(0,30);

        List<Interval> intervals = new ArrayList<>();
        intervals.add(in1);
        intervals.add(in2);
        intervals.add(in3);

//        Interval[] intervals = {in1, in2,in3};

        System.out.println(canAttendMeetings(intervals));
    }


    public static boolean canAttendMeetings(List<Interval> intervals) {
        /**
         * @param intervals: an array of meeting time intervals
         * @return: if a person could attend all meetings
         */
        // Write your code here
        if(intervals == null) return false;

        intervals.sort(Comp);

//        Arrays.sort(intervals, Comp);
        for(int i=0; i<intervals.size(); i++){
            if(intervals.get(i).end > intervals.get(i + 1).start){
                return false;
            }
        }

        return true;
    }

    static Comparator<Interval> Comp = new Comparator<Interval>(){

        @Override
        public int compare(Interval a, Interval b){
            return a.start - b.start;
        }
    };

}

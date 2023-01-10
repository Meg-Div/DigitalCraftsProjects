/*-------------------------------
            ShakeBall
---------------------------------
- index: int
- response: string
- count: int
- OUTLOOK: const vector <string>
---------------------------------
+ ShakeBall()
+ print() : void
+ firstShake() : void
+ nextShake() : void
+ check() : void
-------------------------------*/

#include <iostream>
#include <vector>
#include <chrono>
#include <thread>

using namespace std;

class ShakeBall {
  private:
	  string input;
	  const vector < string > OUTLOOK = {
	    "It is certain.",
	    "It is decidedly so.",
	    "Without a doubt.",
	    "Yes definitely.",
	    "You may rely on it.",
	    "As I see it, yes.",
	    "Most likely.",
	    "Outlook good.",
	    "Yes.",
	    "Signs point to yes.",
	    "Reply hazy, try again.",
	    "Ask again later.",
	    "Better not tell you now.",
	    "Cannot predict now.",
	    "Concentrate and ask again.",
	    "Don't count on it.",
	    "My reply is no.",
	    "My sources say no.",
	    "Outlook not so good.",
	    "Very doubtful."
  };

  public: ShakeBall() {}
  void print();
  void nextShake();
  void firstShake();
  void check(string input);
};

//ShakeBall::print()
//Inputs: none
//Returns: void
void ShakeBall::print() {
	srand(time(0));
  cout << "\n\xf0\x9f\x8e\xb1";
  cout << "  Magic8Ball predicts: \n\n";
  cout << "\t\t" << OUTLOOK[rand() % (OUTLOOK.size())];
	cout << endl;
	nextShake();
}

//ShakeBall::nextShake()
//Inputs: None
//Returns: void
void ShakeBall::nextShake() {	
  cout << "\nShake ball again? Y/N: ";
  cin >> input;
	check(input);
}

//ShakeBall::firstShake()
//Inputs: None
//Returns: void
void ShakeBall::firstShake() {	
  cout << "\nWould you like to shake ";
	cout << "the Magic8Ball? Y/N: " << endl;
  cin >> input;
	check(input);
}

//ShakeBall::check()
//Inputs: String input
//Returns: void
void ShakeBall::check(string input) {
	input[0] = toupper(input[0]);

  if (input != "Y" && input != "N") {
    cout << "\nEnter in Y/N" << endl;
    input = "Y";
		nextShake();
		}
	else if (input == "Y") {
		cout << "\nAsk your question" << endl;
    this_thread::sleep_for(2s);
		print();
  }
}

//driver code
int main() {
  ShakeBall ball;
	
	ball.firstShake();

  return 0;
}
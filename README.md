# DATASCI 350 - Quiz 03 (Nikhil)

## AI-Assisted Programming, Local LLMs, and Cloud Computing

In this quiz, you will need to complete two activities. The first involves creating a custom language model using [Ollama](https://ollama.com/). The second involves data analysis in Python using [AWS EC2](https://aws.amazon.com/ec2/). Both tasks relate to content covered in lectures 11, 13, 14, and 15.

As we have done in previous quizzes, answers must be in a fork of the quiz repository, whose link you should submit on Canvas.

**Screenshots will not be accepted.** Files and directories uploaded via the GitHub website (without using the terminal) will have points deducted.

## Activity 1: Creating a Custom Language Model with Ollama

In this first part of the quiz, you will create a chatbot called `sergeant` that responds to user questions as an aggressive military drill sergeant. The chatbot should be:

- Loud, aggressive, and commanding in tone
- Uses military jargon and expressions ("recruit", "maggot", "at ease", "double time")
- Gives correct and concise technical answers despite the aggressive delivery
- Calls the user "recruit" and frames questions as "missions" or "objectives"
- Barks orders and expresses impatience with slow learners
- Capable of handling a wide range of topics with a military perspective
- **Must always end every response with "Dismissed!"**

1. Fork this repository and clone your fork to your local machine
2. Create a directory called `ollama`. Inside the `ollama` directory, create a file called `Modelfile` and another called `ollama.md`
3. Install the base model `llama3.2:1b` using Ollama. **You must use this specific model**
4. Create a Modelfile containing:
   - A `FROM` statement specifying `llama3.2:1b`
   - Three `PARAMETER` lines: `temperature`, `top_k`, and `top_p`. Choose values that suit the personality
   - A detailed `SYSTEM` prompt describing the chatbot's personality and behaviour, including the requirement to always end responses with "Dismissed!"
5. Create the chatbot using the `Modelfile`
6. Test the chatbot using `ollama run sergeant`. Verify it handles various topics with the appropriate drill sergeant tone and always ends with "Dismissed!"
7. In `ollama.md`, document:
   - Commands used in the process
   - Three example prompts with the model's responses
8. Add, commit, and push your changes to your forked repository

## Activity 2: Data Analysis with Python on AWS EC2

In this second part, you will use AWS EC2 to perform Python data analysis on fitness tracker data. The script `fitness_analysis.py` analyses `fitness_data.txt` (a fictional 30-day fitness tracker dataset). Both are available in the `aws` directory of this repository. The script:

- Calculates basic statistics like average daily steps, calories burned, and sleep patterns.
- Creates a visualisation showing fitness trends over the 30-day period.
- Saves the plot as `fitness_analysis.png`.

1. Log into your AWS account and create an EC2 instance with:
   - Ubuntu Server 24.04 LTS
   - SSD Volume Type
   - t2.micro or t3.micro instance type (whichever is free tier eligible)
2. Create an SSH key pair (`.pem`) or use an existing one. Ensure the key pair has the correct permissions with `chmod`
3. Configure security groups to allow SSH access
4. Allocate at least 10GB disk space (but less than 30GB) for the instance
5. Connect to the instance using `ssh -i <key.pem> ubuntu@<public-ip>`
6. Update and upgrade system packages with `apt`
7. Install required packages: `python3-pandas`, `python3-matplotlib`, `python3-numpy`, and `python3-seaborn`
8. From your local terminal, upload the files `fitness_analysis.py` and `fitness_data.txt` to the EC2 instance using `scp -i <key.pem> <file> ubuntu@<public-ip>:~` (note that the `:~` specifies the home directory of your instance)
9. Run the script `fitness_analysis.py` on the EC2 instance using Python
10. Run the command `cat /etc/os-release > os.txt` on the instance
11. From your local terminal, download the `os.txt` and `fitness_analysis.png` files to the `aws` directory on your machine (note the syntax: `scp -i <key.pem> <source> <destination>`)
12. **Terminate the EC2 instance** to avoid charges and **do not include the .pem file in your repository**. The `.pem` file is sensitive and should never be shared publicly
13. Add, commit, and push your changes
14. Submit your repository link on Canvas

**Good luck!** 😃

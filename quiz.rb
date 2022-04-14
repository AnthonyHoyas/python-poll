class Question 
    attr_accessor :prompt, :awnser
    def initialize(prompt, awnser)
        @prompt = prompt
        @awnser = awnser
    end
end


p1 = "What color is my T-shirt ? (a) Blue (b)Red (c) Yellow \n"
p2 = "What color is your hat ? (a) Blue (b)Red (c) Yellow \n"
p3 = "What color is a banana ? (a) Blue (b)Red (c) Yellow \n"

questions = [
    Question.new(p1, "a"),
    Question.new(p2, "b"),
    Question.new(p3, "c"),
]

def run_test(questions)
    awnser = ""
    score = 0
    for question in questions
        puts question.prompt
        awnser = gets.chomp()
        if awnser == question.awnser
            score += 1
        end
    end
    puts('You got' + score.to_s + "/" + questions.length().to_s)
end

run_test(questions)
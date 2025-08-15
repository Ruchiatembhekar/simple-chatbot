import random
import re

class SimpleChatbot:
    def __init__(self):
        self.name = "ChatBot"
        self.user_name = ""
        
        # Predefined responses for different categories
        self.greetings = [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Greetings! How are you doing?",
            "Hey! Nice to meet you!"
        ]
        
        self.goodbyes = [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! It was nice talking to you!",
            "Farewell! Hope to chat again soon!"
        ]
        
        self.how_are_you_responses = [
            "I'm doing great, thank you for asking!",
            "I'm functioning perfectly! How about you?",
            "I'm excellent! Ready to help you with anything!",
            "I'm doing wonderful! What about you?"
        ]
        
        self.help_responses = [
            "I can help you with basic conversations, answer simple questions, or just chat!",
            "I'm here to assist you! You can ask me about the weather, time, or just have a casual chat.",
            "I can help with basic queries, have conversations, or provide simple information!"
        ]
        
        self.unknown_responses = [
            "I'm not sure I understand. Can you rephrase that?",
            "That's interesting! Can you tell me more?",
            "I'm still learning. Could you explain that differently?",
            "Hmm, I don't quite get that. Can you be more specific?"
        ]

    def preprocess_input(self, user_input):
        """Clean and prepare user input for processing"""
        # Convert to lowercase and strip whitespace
        processed = user_input.lower().strip()
        # Remove extra spaces
        processed = re.sub(r'\s+', ' ', processed)
        return processed

    def get_response(self, user_input):
        """Generate response based on user input using if-elif-else logic"""
        processed_input = self.preprocess_input(user_input)
        
        # Greeting patterns
        if any(word in processed_input for word in ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']):
            return random.choice(self.greetings)
        
        # Goodbye patterns
        elif any(word in processed_input for word in ['bye', 'goodbye', 'see you', 'farewell', 'exit', 'quit']):
            return random.choice(self.goodbyes)
        
        # How are you patterns
        elif any(phrase in processed_input for phrase in ['how are you', 'how do you do', 'how are things', 'what\'s up']):
            return random.choice(self.how_are_you_responses)
        
        # Name-related queries
        elif 'what is your name' in processed_input or 'your name' in processed_input:
            return f"My name is {self.name}! What's your name?"
        
        elif 'my name is' in processed_input:
            # Extract name from input
            name_match = re.search(r'my name is (\w+)', processed_input)
            if name_match:
                self.user_name = name_match.group(1).title()
                return f"Nice to meet you, {self.user_name}!"
            else:
                return "Nice to meet you!"
        
        # Help requests
        elif any(word in processed_input for word in ['help', 'assist', 'support']):
            return random.choice(self.help_responses)
        
        # Age-related queries
        elif 'how old' in processed_input or 'your age' in processed_input:
            return "I'm a chatbot, so I don't have an age in the traditional sense. But I was created recently!"
        
        # Weather queries (simple responses)
        elif 'weather' in processed_input:
            return "I can't check real weather, but I hope it's nice where you are! You might want to check a weather app for accurate information."
        
        # Time queries
        elif 'time' in processed_input and any(word in processed_input for word in ['what', 'current', 'now']):
            return "I can't tell the current time, but you can check your device's clock!"
        
        # Compliments
        elif any(word in processed_input for word in ['good', 'great', 'awesome', 'amazing', 'wonderful']):
            return "Thank you! That's very kind of you to say!"
        
        # Questions about capabilities
        elif 'what can you do' in processed_input or 'your capabilities' in processed_input:
            return "I'm a simple chatbot! I can have basic conversations, respond to greetings, and answer simple questions. I'm still learning!"
        
        # Favorite things
        elif 'favorite' in processed_input:
            return "As a chatbot, I don't have personal preferences, but I enjoy having conversations with people like you!"
        
        # Thank you responses
        elif any(word in processed_input for word in ['thank', 'thanks']):
            return "You're welcome! Happy to help!"
        
        # Yes/No responses
        elif processed_input in ['yes', 'yeah', 'yep', 'sure']:
            return "Great! What would you like to talk about?"
        
        elif processed_input in ['no', 'nope', 'not really']:
            return "That's okay! Is there anything else you'd like to discuss?"
        
        # Default response for unknown inputs
        else:
            return random.choice(self.unknown_responses)

    def start_conversation(self):
        """Main conversation loop"""
        print("=" * 50)
        print(f"Welcome to {self.name}!")
        print("Type 'quit', 'exit', or 'bye' to end the conversation.")
        print("=" * 50)
        
        while True:
            try:
                # Get user input
                user_input = input("\nYou: ").strip()
                
                # Check for empty input
                if not user_input:
                    print(f"{self.name}: Please say something!")
                    continue
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print(f"{self.name}: {random.choice(self.goodbyes)}")
                    break
                
                # Get and display response
                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye! Thanks for chatting!")
                break
            except Exception as e:
                print(f"{self.name}: Sorry, I encountered an error. Let's try again!")

# Main execution
if __name__ == "__main__":
    # Create chatbot instance
    chatbot = SimpleChatbot()
    
    # Start the conversation
    chatbot.start_conversation()
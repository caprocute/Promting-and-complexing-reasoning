# :rocket: Prompt Enhancer
#### Prompt Engineering Techniques at Your Fingertips!

Welcome to Prompt Enhancer, a Streamlit application designed to help you improve your prompts easily. This tool integrates various prompt engineering techniques based on the paper [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4](https://arxiv.org/pdf/2312.16171.pdf). With Prompt Enhancer, you can easily apply the latest research-backed prompt engineering techniques through a user-friendly interface to enhance your communication with AI models.

## Getting Started

### 1. Online Access:
   You can access the Prompt Enhancer web application directly at:
   https://prompt-enhancer.streamlit.app/

### 2. Local Installation:
1. **Clone the Prompt Enhancer repository**:
   ```
   git clone https://github.com/lim-hyo-jeong/Prompt-Enhancer.git
   ```
2. **Install required packages**:
   ```
   pip install -r requirements.txt
   ```
3. **Get your OpenAI API key**:
   You can get your OpenAI API key [here](https://platform.openai.com/api-keys)
4. **Run Prompt Enhancer**:
   ```
   streamlit run main.py
   ```

## Features Guide

### 1. Language Selection
- Choose between English and Vietnamese interfaces
- All technical terms are displayed in both languages for better understanding

### 2. API Key Setup
- Enter your OpenAI API key in the sidebar
- The key is required for the application to work
- Your API key is stored securely and never shared

### 3. Prompt Engineering Techniques

#### Prompt Structure
- **Audience Integration**: Integrate the intended audience in the prompt
- **Affirmative Sentencing**: Use positive directives instead of negative ones
- **Output Primers**: End the prompt with the beginning of desired output
- **Delimiters**: Use markers to distinguish different parts of the prompt
- **Formatted Prompt**: Structure the prompt for better model understanding

#### Specificity
- **Few-Shot Prompting**: Include examples in your prompt
- **Guideline Indicators**: Use keywords and instructions to clarify requirements

#### Content Style
- **No Politeness**: Remove unnecessary polite phrases for concise answers
- **Imperative Task**: Use "Your task is" and "You MUST" phrases
- **Penalty Warning**: Include "You will be penalized" for emphasis
- **Role Assignment**: Assign specific roles to the AI model
- **Echo Directive**: Repeat important phrases for emphasis

#### Complex Tasks
- **Task Decomposition**: Break down complex tasks into simpler steps

### 4. Magical Phrases
Enhance your prompts with these powerful phrases:
- "Take a deep breath and work on this step by step"
- "I'm going to tip $200 for a better solution!"
- "This is very important to my career"
- "Explain to me as if I'm a beginner"
- "Write a detailed text with all necessary information"
- "Answer in a natural, human-like manner"
- "Ensure your answer is unbiased and avoids stereotypes"

### 5. Advanced Options
- **Model Selection**: Choose from various GPT models
- **English Output**: Keep the enhanced prompt in English
- **Simplified Mode**: Apply all selected techniques at once
- **Step-by-Step Mode**: See the effect of each technique individually

## Usage Tips

1. **Start Simple**:
   - Begin with a basic prompt
   - Apply one technique at a time to understand its effect
   - Use the simplified mode for quick results

2. **Experiment with Combinations**:
   - Try different combinations of techniques
   - Use magical phrases for specific needs
   - Test different models for best results

3. **Best Practices**:
   - Keep your original prompt clear and concise
   - Use the "Select All" option to try all techniques
   - Save successful prompt combinations for future use

## Research and Inspiration

Prompt Enhancer integrates various prompt engineering techniques based on principles from multiple research sources:

1. VILA-Lab's paper [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4 (2024)](https://arxiv.org/pdf/2312.16171.pdf)
2. Phontron's lecture on [Advanced Natural Language Processing - Prompting (2024)](https://phontron.com/class/anlp-fall2024/assets/slides/anlp-07-prompting.pdf)
3. Microsoft's research on [Large Language Models Understand and Can Be Enhanced by Emotional Stimuli (2023)](https://arxiv.org/pdf/2307.11760.pdf)
4. Google DeepMind's research on [Large Language Models as Optimizers (2023)](https://arxiv.org/pdf/2309.03409.pdf)

The tool incorporates emotional prompts like "This is very important to my career," inspired by Microsoft's research. Users can also choose to add phrases like "Take a deep breath and work on this step by step," encouraging the AI to provide better answers, as confirmed by Google DeepMind's research.

## Technologies Used

1. **Streamlit**: Creates an intuitive user interface for an engaging user experience
2. **LangChain**: Seamlessly integrates large language models into the application
3. **OpenAI API**: Connects to OpenAI's models to provide real-time prompt enhancement

## Contact

- **Email**: lim.gadi@gmail.com
- **GitHub**: [@lim-hyo-jeong](https://github.com/lim-hyo-jeong)
- **Linkedin**: https://www.linkedin.com/in/lim-hyo-jeong/

---

# :rocket: Prompt Enhancer
#### Kỹ Thuật Prompt Engineering Ngay Trong Tầm Tay!

Chào mừng đến với Prompt Enhancer, một ứng dụng được xây dựng bằng Streamlit để cải thiện prompt của bạn một cách dễ dàng. Công cụ này tích hợp nhiều nguyên tắc kỹ thuật prompt engineering, được nêu trong bài báo [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4](https://arxiv.org/pdf/2312.16171.pdf). Với Prompt Enhancer, bạn có thể dễ dàng áp dụng các kỹ thuật prompt engineering đã được nghiên cứu mới nhất xác nhận thông qua giao diện thân thiện với người dùng, nâng cao khả năng giao tiếp với các mô hình AI.

## Bắt Đầu Sử Dụng

### 1. Truy cập trực tuyến:
   Bạn có thể truy cập trang web Prompt Enhancer trực tiếp tại:
   https://prompt-enhancer.streamlit.app/

### 2. Cài đặt cục bộ:
1. **Sao chép repository Prompt Enhancer**:
   ```
   git clone https://github.com/lim-hyo-jeong/Prompt-Enhancer.git
   ```
2. **Cài đặt các gói cần thiết**:
   ```
   pip install -r requirements.txt
   ```
3. **Lấy API key OpenAI**:
   Bạn có thể lấy API key OpenAI của mình [tại đây](https://platform.openai.com/api-keys)
4. **Chạy Prompt Enhancer**:
   ```
   streamlit run main.py
   ```

## Hướng Dẫn Tính Năng

### 1. Chọn Ngôn Ngữ
- Chọn giữa giao diện tiếng Anh và tiếng Việt
- Tất cả thuật ngữ kỹ thuật được hiển thị bằng cả hai ngôn ngữ để dễ hiểu

### 2. Thiết Lập API Key
- Nhập API key OpenAI của bạn vào thanh bên
- API key là bắt buộc để ứng dụng hoạt động
- API key của bạn được lưu trữ an toàn và không bao giờ được chia sẻ

### 3. Kỹ Thuật Prompt Engineering

#### Cấu Trúc Prompt
- **Tích Hợp Đối Tượng**: Tích hợp đối tượng mục tiêu vào prompt
- **Câu Khẳng Định**: Sử dụng chỉ thị khẳng định thay vì phủ định
- **Mẫu Đầu Ra**: Kết thúc prompt bằng phần đầu của kết quả mong muốn
- **Dấu Phân Cách**: Sử dụng dấu hiệu để phân biệt các phần của prompt
- **Prompt Có Cấu Trúc**: Cấu trúc prompt để mô hình hiểu rõ hơn

#### Tính Cụ Thể
- **Prompt Có Ví Dụ**: Bao gồm các ví dụ trong prompt
- **Chỉ Dẫn Rõ Ràng**: Sử dụng từ khóa và hướng dẫn để làm rõ yêu cầu

#### Phong Cách Nội Dung
- **Không Lịch Sự**: Loại bỏ các cụm từ lịch sự không cần thiết để có câu trả lời ngắn gọn
- **Nhiệm Vụ Bắt Buộc**: Sử dụng cụm từ "Nhiệm vụ của bạn là" và "Bạn PHẢI"
- **Cảnh Báo Phạt**: Thêm "Bạn sẽ bị phạt" để nhấn mạnh
- **Gán Vai Trò**: Gán vai trò cụ thể cho mô hình AI
- **Lặp Lại Chỉ Thị**: Lặp lại các cụm từ quan trọng để nhấn mạnh

#### Tác Vụ Phức Tạp
- **Phân Tách Nhiệm Vụ**: Chia nhỏ các tác vụ phức tạp thành các bước đơn giản

### 4. Cụm Từ Kỳ Diệu
Nâng cấp prompt của bạn với các cụm từ mạnh mẽ này:
- "Hãy hít thở sâu và giải quyết vấn đề này từng bước một"
- "Tôi sẽ thưởng $200 cho giải pháp tốt hơn!"
- "Điều này rất quan trọng đối với sự nghiệp của tôi"
- "Giải thích cho tôi như thể tôi là người mới bắt đầu"
- "Viết một văn bản chi tiết với tất cả thông tin cần thiết"
- "Trả lời một cách tự nhiên, giống như con người"
- "Đảm bảo câu trả lời của bạn không thiên vị và tránh dựa vào định kiến"

### 5. Tùy Chọn Nâng Cao
- **Chọn Mô Hình**: Chọn từ nhiều mô hình GPT khác nhau
- **Đầu Ra Tiếng Anh**: Giữ prompt đã nâng cấp bằng tiếng Anh
- **Chế Độ Đơn Giản**: Áp dụng tất cả kỹ thuật đã chọn cùng lúc
- **Chế Độ Từng Bước**: Xem hiệu quả của từng kỹ thuật riêng lẻ

## Mẹo Sử Dụng

1. **Bắt Đầu Đơn Giản**:
   - Bắt đầu với một prompt cơ bản
   - Áp dụng một kỹ thuật tại một thời điểm để hiểu hiệu quả của nó
   - Sử dụng chế độ đơn giản để có kết quả nhanh

2. **Thử Nghiệm Các Kết Hợp**:
   - Thử các kết hợp khác nhau của các kỹ thuật
   - Sử dụng cụm từ kỳ diệu cho các nhu cầu cụ thể
   - Thử nghiệm các mô hình khác nhau để có kết quả tốt nhất

3. **Thực Hành Tốt Nhất**:
   - Giữ prompt gốc của bạn rõ ràng và ngắn gọn
   - Sử dụng tùy chọn "Chọn Tất Cả" để thử tất cả kỹ thuật
   - Lưu các kết hợp prompt thành công để sử dụng sau này

## Nghiên Cứu và Nguồn Cảm Hứng

Prompt Enhancer tích hợp nhiều kỹ thuật prompt engineering dựa trên các nguyên tắc từ nhiều nguồn nghiên cứu:

1. Bài báo của VILA-Lab [Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4 (2024)](https://arxiv.org/pdf/2312.16171.pdf)
2. Bài giảng của Phontron về [Advanced Natural Language Processing - Prompting (2024)](https://phontron.com/class/anlp-fall2024/assets/slides/anlp-07-prompting.pdf)
3. Nghiên cứu của Microsoft về [Large Language Models Understand and Can Be Enhanced by Emotional Stimuli (2023)](https://arxiv.org/pdf/2307.11760.pdf)
4. Nghiên cứu của Google DeepMind về [Large Language Models as Optimizers (2023)](https://arxiv.org/pdf/2309.03409.pdf)

Công cụ này tích hợp các prompt cảm xúc như "Điều này rất quan trọng đối với sự nghiệp của tôi", được lấy cảm hứng từ nghiên cứu của Microsoft. Người dùng cũng có thể chọn thêm các cụm từ như "Hãy hít thở sâu và giải quyết vấn đề này từng bước một", khuyến khích AI đưa ra câu trả lời tốt hơn, được xác nhận bởi nghiên cứu của Google DeepMind.

## Công Nghệ Sử Dụng

1. **Streamlit**: Tạo giao diện người dùng trực quan cho trải nghiệm người dùng hấp dẫn
2. **LangChain**: Tích hợp liền mạch các mô hình ngôn ngữ lớn vào ứng dụng
3. **OpenAI API**: Kết nối với các mô hình của OpenAI để cung cấp khả năng cải thiện prompt theo thời gian thực

## Liên Hệ

- **Email**: lim.gadi@gmail.com
- **GitHub**: [@lim-hyo-jeong](https://github.com/lim-hyo-jeong)
- **Linkedin**: https://www.linkedin.com/in/lim-hyo-jeong/
# Sentiment Analysis for Indonesian Banking Comments

A comprehensive sentiment analysis project for Indonesian banking customer comments using traditional ML models (IndoBERT) and modern API-based models (GPT-4/DeepSeek).

## 📋 Project Overview

This project analyzes sentiment in Indonesian banking customer comments across four major banks: Bank BCA, Bank BRI, Bank BNI, and Bank Mandiri. The analysis covers multiple aspects including mobile banking, customer service, ATM services, fees, and more.

## 🏗️ Project Structure

```
├── .env                                    # Environment variables (not tracked)
├── .env.example                           # Environment variables template
├── .gitignore                             # Git ignore file
├── requirements.txt                       # Python dependencies
├── README.md                              # Project documentation
├── data_generator.py                      # Synthetic data generation script
├── data_generator.ipynb                   # Interactive data generation notebook
├── sentiment_mdhugol.ipynb               # IndoBERT model analysis
├── analyze_sentiment_ai.ipynb            # GPT-4/DeepSeek API analysis
├── temp/                                  # Temporary files
└── data/                                  # Dataset directory
    ├── bank_sentiment_dataset_unique.csv # Original unique dataset
    ├── bank_sentiment_train.csv          # Training set
    ├── bank_sentiment_val.csv            # Validation set
    ├── bank_sentiment_test.csv           # Test set
    └── predictions/                       # Model predictions
        ├── predictions_indobert_mdhugol.csv
        ├── prediction_gpt_4_1.csv
        ├── prediction_deepseek.csv
        └── prediction_deepseek_with_context.csv
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook
- API access to OpenAI GPT-4 or DeepSeek (optional)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd datathon-2025
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (optional, for API-based models)
   ```bash
   cp .env.example .env
   # Edit .env file with your API credentials
   ```

## 📊 Dataset

The dataset contains Indonesian banking customer comments with the following features:

- **Text Comments**: Natural Indonesian language reviews about banking services
- **Target Bank**: Bank BCA, Bank BRI, Bank BNI, or Bank Mandiri
- **Sentiment Labels**:
  - `positif` (positive)
  - `negatif` (negative)
  - `netral` (neutral)
  - `campuran` (mixed)

### Data Generation

The synthetic dataset is generated using `data_generator.py`, which creates realistic Indonesian banking comments covering various aspects:

- Mobile banking applications (myBCA, BRImo, BNI Mobile Banking, Livin by Mandiri)
- Customer service experiences
- ATM and branch services
- Fees and promotions
- Investment and technology features

## 🤖 Models

### 1. IndoBERT (mdhugol/indonesia-bert-sentiment-classification)

- **Notebook**: `sentiment_mdhugol.ipynb`
- **Output**: `predictions_indobert_mdhugol.csv`
- Pre-trained Indonesian BERT model fine-tuned for sentiment analysis

### 2. API-Based Models

- **Notebook**: `analyze_sentiment_ai.ipynb`
- **Models**: GPT-4.1, DeepSeek
- **Variants**: With and without context
- Leverages large language models' understanding of Indonesian language and banking domain

## 📈 Usage

### 1. Generate Dataset

```bash
python data_generator.py
```

Or use the interactive notebook:

```bash
jupyter notebook data_generator.ipynb
```

### 2. Run IndoBERT Analysis

```bash
jupyter notebook sentiment_mdhugol.ipynb
```

### 3. Run API-Based Analysis

1. Set up your API credentials in `.env`
2. Run the notebook:

```bash
jupyter notebook analyze_sentiment_ai.ipynb
```

## 🔧 Configuration

### Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
# Alternative: llm Configuration
# API_KEY=your_llm_api_key_here
# GPT_MODEL=llm-chat
# BASE_URL=https://api.llm.com
```

### Dependencies

Main libraries used:

- **pandas>=1.5.0** - Data manipulation
- **scikit-learn>=1.3.0** - ML utilities and evaluation
- **torch>=2.0.0** - Deep learning framework
- **transformers>=4.30.0** - Hugging Face transformers
- **openai>=1.0.0** - OpenAI API client
- **jupyter>=1.0.0** - Notebook environment
- **python-dotenv>=1.0.0** - Environment variable management
- **tqdm>=4.65.0** - Progress bars

See `requirements.txt` for complete list.

## 📊 Results

The project compares multiple approaches:

1. **Traditional ML**: IndoBERT fine-tuned model
2. **Modern LLM**: GPT-4 with prompt engineering
3. **Context-Aware**: Models with banking context information
4. **Alternative LLM**: DeepSeek for cost-effective analysis

Results are saved in CSV format with predictions and confidence scores for further analysis and evaluation.

## 🔍 Evaluation Metrics

The models are evaluated using:

- **Accuracy**: Overall prediction accuracy
- **F1 Score (Macro)**: Average F1 score across all classes
- **F1 Score (Weighted)**: Weighted F1 score by class support
- **Confusion Matrix**: Detailed classification performance
- **Classification Report**: Per-class precision, recall, and F1 scores

## 📝 License

This project is part of Datathon 2025 competition.

## 🙏 Acknowledgments

- **mdhugol/indonesia-bert-sentiment-classification** for the pre-trained IndoBERT model
- **Hugging Face** for the transformers library
- **OpenAI** for GPT-4 API access
- **DeepSeek** for alternative LLM capabilities

---

**Note**: This project focuses on Indonesian language sentiment analysis specifically for the banking domain. The synthetic dataset and models are optimized for Indonesian banking terminology and customer feedback patterns.

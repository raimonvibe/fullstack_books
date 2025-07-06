import re
from typing import List, Set

SPAM_WORDS: Set[str] = {
    'viagra', 'cialis', 'pharmacy', 'pills', 'medication', 'drugs',
    'casino', 'gambling', 'poker', 'lottery', 'jackpot', 'winner',
    'free money', 'cash prize', 'get rich', 'make money fast',
    'work from home', 'earn money', 'business opportunity',
    'click here', 'visit now', 'act now', 'limited time',
    'special offer', 'discount', 'sale', 'cheap', 'lowest price',
    'buy now', 'order now', 'call now', 'subscribe',
    
    'porn', 'xxx', 'adult', 'sex', 'nude', 'naked',
    'escort', 'dating', 'hookup', 'singles',
    
    'damn', 'hell', 'crap', 'stupid', 'idiot', 'moron',
    'suck', 'sucks', 'hate', 'kill', 'die', 'death',
    
    'mlm', 'pyramid scheme', 'get paid', 'easy money',
    'no experience', 'guaranteed', 'risk free',
    'weight loss', 'lose weight', 'diet pills',
    'enlargement', 'enhancement', 'miracle',
    
    'nigerian prince', 'inheritance', 'lottery winner',
    'bank transfer', 'wire transfer', 'western union',
    'paypal', 'bitcoin', 'cryptocurrency', 'investment',
    'loan', 'credit', 'debt', 'refinance',
    
    'http://', 'https://', 'www.', '.com', '.net', '.org',
    'bit.ly', 'tinyurl', 'shorturl', 'link',
    
    'aaa', 'bbb', 'ccc', '!!!', '???', '***',
    'urgent', 'important', 'congratulations', 'winner',
    
    'follow me', 'like and share', 'subscribe', 'influencer',
    'social media', 'instagram', 'facebook', 'twitter',
    'youtube', 'tiktok', 'snapchat',
    
    'spam', 'junk', 'fake', 'scam', 'fraud', 'phishing',
    'virus', 'malware', 'trojan', 'hack', 'hacker'
}

def contains_spam(text: str) -> bool:
    """
    Check if the given text contains spam words.
    
    Args:
        text (str): The text to check for spam
        
    Returns:
        bool: True if spam is detected, False otherwise
    """
    if not text or not isinstance(text, str):
        return False
    
    text_lower = text.lower()
    
    text_normalized = ' '.join(text_lower.split())
    
    for spam_word in SPAM_WORDS:
        if re.search(r'\b' + re.escape(spam_word) + r'\b', text_normalized):
            return True
        
        if len(spam_word) > 3 and spam_word in text_normalized:
            return True
    
    if _has_suspicious_patterns(text_normalized):
        return True
    
    return False

def _has_suspicious_patterns(text: str) -> bool:
    """
    Check for suspicious patterns that might indicate spam.
    
    Args:
        text (str): The normalized text to check
        
    Returns:
        bool: True if suspicious patterns are found
    """
    if re.search(r'(.)\1{4,}', text):  # Same character repeated 5+ times
        return True
    
    if re.search(r'[!?]{3,}', text):  # 3+ exclamation/question marks
        return True
    
    if len(text) > 10 and sum(1 for c in text if c.isupper()) / len(text) > 0.7:
        return True
    
    if re.search(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text):  # Phone number pattern
        return True
    
    return False

def get_spam_message() -> str:
    """
    Get a user-friendly message to display when spam is detected.
    
    Returns:
        str: The spam detection message
    """
    return "Your content contains inappropriate or spam-like words and cannot be submitted. Please revise your text and try again."

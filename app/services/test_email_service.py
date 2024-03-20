import unittest
from app.services.email_service import send_email

class TestEmailService(unittest.TestCase):
    
    def test_send_email(self):
        # Test with valid inputs
        result = send_email('test@example.com', 'Test Subject', 'test_template', name='John')
        self.assertIsNone(result)
        
        # Test with invalid email
        with self.assertRaises(Exception):
            send_email('invalid_email', 'Test Subject', 'test_template')
            
        # Test with missing template
        with self.assertRaises(Exception):
            send_email('test@example.com', 'Test Subject', 'missing_template')
            

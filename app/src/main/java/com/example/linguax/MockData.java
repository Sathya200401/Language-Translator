package com.example.linguax;

import java.util.HashMap;
import java.util.Map;

public class MockData {
    // Map<TargetLanguage, Map<EnglishText, TranslatedText>>
    private static final Map<String, Map<String, String>> languageMap = new HashMap<>();

    static {
        // --- TELUGU ---
        Map<String, String> telugu = new HashMap<>();
        telugu.put("hello, how are you?", "నమస్కారం, మీరు ఎలా ఉన్నారు?");
        telugu.put("hello", "నమస్కారం");
        telugu.put("i love learning new languages.", "నాకు కొత్త భాషలు నేర్చుకోవడం ఇష్టం.");
        telugu.put("break every language barrier", "అన్ని భాషా అడ్డంకులను బద్దలు కొట్టండి");
        telugu.put("what is your name?", "మీ పేరు ఏమిటి?");
        telugu.put("can you help me please?", "దయచేసి నాకు సహాయం చేయగలరా?");
        telugu.put("where is the nearest restaurant?", "దగ్గరలో ఉన్న రెస్టారెంట్ ఎక్కడ ఉంది?");
        telugu.put("thank you very much.", "చాలా ధన్యవాదాలు.");
        telugu.put("good morning!", "శుభోదయం!");
        telugu.put("see you later.", "మళ్ళీ కలుద్దాం.");
        telugu.put("how much does this cost?", "దీని ధర ఎంత?");
        telugu.put("i don't understand.", "నాకు అర్థం కాలేదు.");
        telugu.put("excuse me.", "క్షమించండి.");
        telugu.put("where is the bathroom?", "బాత్రూమ్ ఎక్కడ ఉంది?");
        telugu.put("i need a doctor.", "నాకు డాక్టర్ కావాలి.");
        telugu.put("how are you?", "మీరు ఎలా ఉన్నారు?");
        telugu.put("i am fine, thank you.", "నేను బాగున్నాను, ధన్యవాదాలు.");
        telugu.put("what time is it?", "సమయం ఎంత?");
        languageMap.put("telugu", telugu);

        // --- SPANISH ---
        Map<String, String> spanish = new HashMap<>();
        spanish.put("hello, how are you?", "Hola, ¿cómo estás?");
        spanish.put("hello", "Hola");
        spanish.put("i love learning new languages.", "Me encanta aprender nuevos idiomas.");
        spanish.put("break every language barrier", "Rompe cada barrera del idioma");
        spanish.put("what is your name?", "¿Cuál es tu nombre?");
        spanish.put("can you help me please?", "¿Puedes ayudarme por favor?");
        spanish.put("where is the nearest restaurant?", "¿Dónde está el restaurante más cercano?");
        spanish.put("thank you very much.", "Muchas gracias.");
        spanish.put("good morning!", "¡Buenos días!");
        spanish.put("see you later.", "Hasta luego.");
        spanish.put("how much does this cost?", "¿Cuánto cuesta esto?");
        spanish.put("i don't understand.", "No entiendo.");
        spanish.put("excuse me.", "Disculpe.");
        spanish.put("where is the bathroom?", "¿Dónde está el baño?");
        spanish.put("i need a doctor.", "Necesito un médico.");
        spanish.put("how are you?", "¿Cómo estás?");
        spanish.put("i am fine, thank you.", "Estoy bien, gracias.");
        spanish.put("what time is it?", "¿Qué hora es?");
        languageMap.put("spanish", spanish);

        // --- FRENCH ---
        Map<String, String> french = new HashMap<>();
        french.put("hello, how are you?", "Bonjour, comment allez-vous?");
        french.put("hello", "Bonjour");
        french.put("i love learning new languages.", "J'adore apprendre de nouvelles langues.");
        french.put("break every language barrier", "Brisez toutes les barrières linguistiques");
        french.put("what is your name?", "Comment vous appelez-vous?");
        french.put("can you help me please?", "Pouvez-vous m'aider s'il vous plaît?");
        french.put("where is the nearest restaurant?", "Où est le restaurant le plus proche?");
        french.put("thank you very much.", "Merci beaucoup.");
        french.put("good morning!", "Bonjour!");
        french.put("see you later.", "À plus tard.");
        french.put("how much does this cost?", "Combien ça coûte?");
        french.put("i don't understand.", "Je ne comprends pas.");
        french.put("excuse me.", "Excusez-moi.");
        french.put("where is the bathroom?", "Où sont les toilettes?");
        french.put("i need a doctor.", "J'ai besoin d'un médecin.");
        french.put("how are you?", "Comment allez-vous?");
        french.put("i am fine, thank you.", "Je vais bien, merci.");
        french.put("what time is it?", "Quelle heure est-il?");
        languageMap.put("french", french);

        // --- JAPANESE ---
        Map<String, String> japanese = new HashMap<>();
        japanese.put("hello, how are you?", "こんにちは、お元気ですか？");
        japanese.put("hello", "こんにちは");
        japanese.put("i love learning new languages.", "新しい言語を学ぶのが大好きです。");
        japanese.put("break every language barrier", "すべての言葉の壁を打ち破る");
        japanese.put("what is your name?", "お名前は何ですか？");
        japanese.put("can you help me please?", "手伝ってくれませんか？");
        japanese.put("where is the nearest restaurant?", "一番近いレストランはどこですか？");
        japanese.put("thank you very much.", "どうもありがとうございます。");
        japanese.put("good morning!", "おはようございます！");
        japanese.put("see you later.", "またね。");
        japanese.put("how much does this cost?", "これはいくらですか？");
        japanese.put("i don't understand.", "わかりません。");
        japanese.put("excuse me.", "すみません。");
        japanese.put("where is the bathroom?", "トイレはどこですか？");
        japanese.put("i need a doctor.", "医者が必要です。");
        japanese.put("how are you?", "お元気ですか？");
        japanese.put("i am fine, thank you.", "私は元気です、ありがとう。");
        japanese.put("what time is it?", "今何時ですか？");
        languageMap.put("japanese", japanese);

        // --- GERMAN ---
        Map<String, String> german = new HashMap<>();
        german.put("hello, how are you?", "Hallo, wie geht es dir?");
        german.put("hello", "Hallo");
        german.put("i love learning new languages.", "Ich liebe es, neue Sprachen zu lernen.");
        german.put("break every language barrier", "Brechen Sie jede Sprachbarriere");
        german.put("what is your name?", "Wie heißt du?");
        german.put("can you help me please?", "Können Sie mir bitte helfen?");
        german.put("where is the nearest restaurant?", "Wo ist das nächste Restaurant?");
        german.put("thank you very much.", "Vielen Dank.");
        german.put("good morning!", "Guten Morgen!");
        german.put("see you later.", "Bis später.");
        german.put("how much does this cost?", "Wie viel kostet das?");
        german.put("i don't understand.", "Ich verstehe nicht.");
        german.put("excuse me.", "Entschuldigung.");
        german.put("where is the bathroom?", "Wo ist die Toilette?");
        german.put("i need a doctor.", "Ich brauche einen Arzt.");
        german.put("how are you?", "Wie geht es dir?");
        german.put("i am fine, thank you.", "Mir geht es gut, danke.");
        german.put("what time is it?", "Wie spät ist es?");
        languageMap.put("german", german);

        // --- ITALIAN ---
        Map<String, String> italian = new HashMap<>();
        italian.put("hello, how are you?", "Ciao, come stai?");
        italian.put("hello", "Ciao");
        italian.put("i love learning new languages.", "Amo imparare nuove lingue.");
        italian.put("break every language barrier", "Abbatti ogni barriera linguistica");
        italian.put("what is your name?", "Come ti chiami?");
        italian.put("can you help me please?", "Puoi aiutarmi per favore?");
        italian.put("where is the nearest restaurant?", "Dov'è il ristorante più vicino?");
        italian.put("thank you very much.", "Grazie mille.");
        italian.put("good morning!", "Buongiorno!");
        italian.put("see you later.", "A dopo.");
        italian.put("how much does this cost?", "Quanto costa questo?");
        italian.put("i don't understand.", "Non capisco.");
        italian.put("excuse me.", "Mi scusi.");
        italian.put("where is the bathroom?", "Dov'è il bagno?");
        italian.put("i need a doctor.", "Ho bisogno di un medico.");
        italian.put("how are you?", "Come stai?");
        italian.put("i am fine, thank you.", "Sto bene, grazie.");
        italian.put("what time is it?", "Che ore sono?");
        languageMap.put("italian", italian);

        // --- HINDI ---
        Map<String, String> hindi = new HashMap<>();
        hindi.put("hello, how are you?", "नमस्ते, आप कैसे हैं?");
        hindi.put("hello", "नमस्ते");
        hindi.put("i love learning new languages.", "मुझे नई भाषाएं सीखना पसंद है।");
        hindi.put("break every language barrier", "हर भाषा की बाधा को तोड़ें");
        hindi.put("what is your name?", "आपका नाम क्या है?");
        hindi.put("can you help me please?", "क्या आप कृपया मेरी मदद कर सकते हैं?");
        hindi.put("where is the nearest restaurant?", "निकटतम रेस्तरां कहाँ है?");
        hindi.put("thank you very much.", "आपका बहुत-बहुत धन्यवाद।");
        hindi.put("good morning!", "सुप्रभात!");
        hindi.put("see you later.", "बाद में मिलते हैं।");
        hindi.put("how much does this cost?", "इसकी कीमत कितनी है?");
        hindi.put("i don't understand.", "मुझे समझ नहीं आया।");
        hindi.put("excuse me.", "माफ़ कीजिए।");
        hindi.put("where is the bathroom?", "शौचालय कहाँ है?");
        hindi.put("i need a doctor.", "मुझे डॉक्टर की ज़रूरत है।");
        hindi.put("how are you?", "आप कैसे हैं?");
        hindi.put("i am fine, thank you.", "मैं ठीक हूँ, धन्यवाद।");
        hindi.put("what time is it?", "समय क्या है?");
        languageMap.put("hindi", hindi);

        // --- KOREAN ---
        Map<String, String> korean = new HashMap<>();
        korean.put("hello, how are you?", "안녕하세요, 잘 지내세요?");
        korean.put("hello", "안녕하세요");
        korean.put("i love learning new languages.", "저는 새로운 언어를 배우는 것을 좋아합니다.");
        korean.put("break every language barrier", "모든 언어 장벽을 허물다");
        korean.put("what is your name?", "이름이 뭐예요?");
        korean.put("can you help me please?", "도와주시겠어요?");
        korean.put("where is the nearest restaurant?", "가장 가까운 식당이 어디인가요?");
        korean.put("thank you very much.", "대단히 감사합니다.");
        korean.put("good morning!", "좋은 아침입니다!");
        korean.put("see you later.", "나중에 봐요.");
        korean.put("how much does this cost?", "이거 얼마예요?");
        korean.put("i don't understand.", "이해가 안 가요.");
        korean.put("excuse me.", "실례합니다.");
        korean.put("where is the bathroom?", "화장실은 어디인가요?");
        korean.put("i need a doctor.", "의사가 필요해요.");
        korean.put("how are you?", "어떻게 지내세요?");
        korean.put("i am fine, thank you.", "저는 잘 지내요, 감사합니다.");
        korean.put("what time is it?", "지금 몇 시예요?");
        languageMap.put("korean", korean);
    }
    
    public static String getTranslation(String input, String targetLanguage) {
        String key = input.toLowerCase().trim();
        String lang = targetLanguage.toLowerCase().trim();

        if (lang.contains("telugu")) lang = "telugu";
        else if (lang.contains("spanish")) lang = "spanish";
        else if (lang.contains("french")) lang = "french";
        else if (lang.contains("japanese")) lang = "japanese";
        else if (lang.contains("german")) lang = "german";
        else if (lang.contains("italian")) lang = "italian";
        else if (lang.contains("hindi")) lang = "hindi";
        else if (lang.contains("korean")) lang = "korean";
        else lang = "spanish"; // Fallback

        Map<String, String> translations = languageMap.get(lang);
        if (translations != null && translations.containsKey(key)) {
            return translations.get(key);
        }
        
        return "Translation not found. Try phrases like 'Hello', 'What is your name?', or 'Thank you very much.'";
    }
}

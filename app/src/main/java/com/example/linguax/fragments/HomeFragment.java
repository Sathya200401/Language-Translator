package com.example.linguax.fragments;

import android.animation.ObjectAnimator;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import com.example.linguax.MockData;
import com.example.linguax.R;

public class HomeFragment extends Fragment {

    private EditText etInput;
    private TextView tvOutput;
    private Button btnTranslate;
    private ImageView btnSwap;
    private TextView tvSourceLang;
    private TextView tvTargetLang;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_home, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        
        etInput = view.findViewById(R.id.etInput);
        tvOutput = view.findViewById(R.id.tvOutput);
        btnTranslate = view.findViewById(R.id.btnTranslate);
        btnSwap = view.findViewById(R.id.btnSwap);
        tvSourceLang = view.findViewById(R.id.tvSourceLang);
        tvTargetLang = view.findViewById(R.id.tvTargetLang);
        ImageView btnCopy = view.findViewById(R.id.btnCopy);
        
        btnCopy.setOnClickListener(v -> {
            String text = tvOutput.getText().toString();
            if (!text.isEmpty() && !text.equals("Translation will appear here...")) {
                android.content.ClipboardManager clipboard = (android.content.ClipboardManager) requireContext().getSystemService(android.content.Context.CLIPBOARD_SERVICE);
                android.content.ClipData clip = android.content.ClipData.newPlainText("Translated Text", text);
                clipboard.setPrimaryClip(clip);
                android.widget.Toast.makeText(requireContext(), "Copied to clipboard", android.widget.Toast.LENGTH_SHORT).show();
            }
        });
        
        tvTargetLang.setOnClickListener(v -> {
            String current = tvTargetLang.getText().toString();
            if (current.contains("Telugu")) tvTargetLang.setText("🇪🇸 Spanish");
            else if (current.contains("Spanish")) tvTargetLang.setText("🇫🇷 French");
            else if (current.contains("French")) tvTargetLang.setText("🇯🇵 Japanese");
            else if (current.contains("Japanese")) tvTargetLang.setText("🇩🇪 German");
            else if (current.contains("German")) tvTargetLang.setText("🇮🇹 Italian");
            else if (current.contains("Italian")) tvTargetLang.setText("🇮🇳 Hindi");
            else if (current.contains("Hindi")) tvTargetLang.setText("🇰🇷 Korean");
            else tvTargetLang.setText("🇮🇳 Telugu");
        });

        btnSwap.setOnClickListener(v -> {
            ObjectAnimator rotation = ObjectAnimator.ofFloat(btnSwap, "rotation", 0f, 180f);
            rotation.setDuration(300);
            rotation.start();
            
            String temp = tvSourceLang.getText().toString();
            tvSourceLang.setText(tvTargetLang.getText().toString());
            tvTargetLang.setText(temp);
        });

        btnTranslate.setOnClickListener(v -> {
            String input = etInput.getText().toString();
            if (input.isEmpty()) {
                input = "hello, how are you?";
                etInput.setText(input);
            }
            
            btnTranslate.setText("Translating...");
            final String textToTranslate = input;
            final String targetLang = tvTargetLang.getText().toString();
            
            new Handler(Looper.getMainLooper()).postDelayed(() -> {
                String translated = MockData.getTranslation(textToTranslate, targetLang);
                tvOutput.setText(translated);
                tvOutput.setTextColor(getResources().getColor(R.color.white, null));
                btnTranslate.setText("Translate ✦");
            }, 1000); // Fake delay for shimmer/loading effect
        });
    }
}

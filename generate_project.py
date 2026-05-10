import os

project_dir = "c:/Users/SATYA GNANESH/OneDrive/Documents/Desktop/Language Translatir"

files = {
    "settings.gradle": """pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "LinguaX"
include ':app'
""",

    "build.gradle": """// Top-level build file
buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:8.1.1'
        classpath 'androidx.navigation:navigation-safe-args-gradle-plugin:2.7.5'
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}
""",

    "gradle.properties": """org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
android.useAndroidX=true
android.enableJetifier=true
""",
    
    "gradle/wrapper/gradle-wrapper.properties": """distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.0-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
""",

    "app/build.gradle": """plugins {
    id 'com.android.application'
    id 'androidx.navigation.safeargs'
}

android {
    namespace 'com.example.linguax'
    compileSdk 34

    defaultConfig {
        applicationId "com.example.linguax"
        minSdk 24
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
    buildFeatures {
        viewBinding true
    }
}

dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.10.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.4'
    implementation 'androidx.navigation:navigation-fragment:2.7.5'
    implementation 'androidx.navigation:navigation-ui:2.7.5'
    
    // Lottie for animations
    implementation 'com.airbnb.android:lottie:6.1.0'
}
""",

    "app/src/main/AndroidManifest.xml": """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.linguax">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.LinguaX">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
""",

    "app/src/main/res/values/colors.xml": """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Deep Navy Blue (#0A0F2C) -->
    <color name="deep_navy">#0A0F2C</color>
    <!-- Electric Blue (#3D5AFE) -->
    <color name="electric_blue">#3D5AFE</color>
    <!-- Soft Purple (#7C4DFF) -->
    <color name="soft_purple">#7C4DFF</color>
    
    <color name="white">#FFFFFF</color>
    <color name="white_translucent">#1AFFFFFF</color>
    <color name="white_translucent_darker">#0DFFFFFF</color>
    
    <color name="text_primary">#FFFFFF</color>
    <color name="text_secondary">#B0BEC5</color>
</resources>
""",

    "app/src/main/res/values/strings.xml": """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">LinguaX</string>
    <string name="subtitle">Break Every Language Barrier</string>
    <string name="powered_by_ai">Powered by AI</string>
</resources>
""",

    "app/src/main/res/values/themes.xml": """<?xml version="1.0" encoding="utf-8"?>
<resources xmlns:tools="http://schemas.android.com/tools">
    <style name="Theme.LinguaX" parent="Theme.MaterialComponents.DayNight.NoActionBar">
        <item name="colorPrimary">@color/electric_blue</item>
        <item name="colorPrimaryVariant">@color/deep_navy</item>
        <item name="colorOnPrimary">@color/white</item>
        <item name="colorSecondary">@color/soft_purple</item>
        <item name="colorSecondaryVariant">@color/soft_purple</item>
        <item name="colorOnSecondary">@color/white</item>
        <item name="android:statusBarColor">@color/deep_navy</item>
        <item name="android:windowBackground">@color/deep_navy</item>
    </style>
</resources>
""",

    "app/src/main/res/drawable/glass_card.xml": """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <solid android:color="@color/white_translucent" />
    <corners android:radius="24dp" />
    <stroke android:width="1dp" android:color="#33FFFFFF" />
</shape>
""",

    "app/src/main/res/drawable/gradient_button.xml": """<?xml version="1.0" encoding="utf-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle">
    <gradient
        android:startColor="@color/electric_blue"
        android:endColor="@color/soft_purple"
        android:angle="0" />
    <corners android:radius="24dp" />
</shape>
""",

    "app/src/main/res/layout/activity_main.xml": """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/deep_navy">

    <androidx.fragment.app.FragmentContainerView
        android:id="@+id/nav_host_fragment"
        android:name="androidx.navigation.fragment.NavHostFragment"
        android:layout_width="0dp"
        android:layout_height="0dp"
        app:layout_constraintBottom_toTopOf="@+id/bottom_navigation"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:defaultNavHost="true"
        app:navGraph="@navigation/nav_graph" />

    <com.google.android.material.bottomnavigation.BottomNavigationView
        android:id="@+id/bottom_navigation"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:background="@color/deep_navy"
        app:itemIconTint="@color/white"
        app:itemTextColor="@color/white"
        app:menu="@menu/bottom_nav_menu"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
""",

    "app/src/main/res/menu/bottom_nav_menu.xml": """<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/homeFragment"
        android:icon="@android:drawable/ic_menu_sort_by_size"
        android:title="Home" />
    <item
        android:id="@+id/historyFragment"
        android:icon="@android:drawable/ic_menu_recent_history"
        android:title="History" />
    <item
        android:id="@+id/favoritesFragment"
        android:icon="@android:drawable/star_on"
        android:title="Favorites" />
    <item
        android:id="@+id/settingsFragment"
        android:icon="@android:drawable/ic_menu_preferences"
        android:title="Settings" />
</menu>
""",

    "app/src/main/res/navigation/nav_graph.xml": """<?xml version="1.0" encoding="utf-8"?>
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/nav_graph"
    app:startDestination="@id/splashFragment">

    <fragment
        android:id="@+id/splashFragment"
        android:name="com.example.linguax.fragments.SplashFragment"
        tools:layout="@layout/fragment_splash">
        <action
            android:id="@+id/action_splash_to_home"
            app:destination="@id/homeFragment"
            app:popUpTo="@id/splashFragment"
            app:popUpToInclusive="true" />
    </fragment>

    <fragment
        android:id="@+id/homeFragment"
        android:name="com.example.linguax.fragments.HomeFragment"
        tools:layout="@layout/fragment_home" />

    <fragment
        android:id="@+id/historyFragment"
        android:name="com.example.linguax.fragments.HistoryFragment"
        tools:layout="@layout/fragment_history" />

    <fragment
        android:id="@+id/favoritesFragment"
        android:name="com.example.linguax.fragments.FavoritesFragment"
        tools:layout="@layout/fragment_favorites" />

    <fragment
        android:id="@+id/settingsFragment"
        android:name="com.example.linguax.fragments.SettingsFragment"
        tools:layout="@layout/fragment_settings" />
</navigation>
""",

    "app/src/main/res/layout/fragment_splash.xml": """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/deep_navy">

    <TextView
        android:id="@+id/tvAppName"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="LinguaX"
        android:textColor="@color/white"
        android:textSize="36sp"
        android:textStyle="bold"
        app:layout_constraintBottom_toTopOf="@+id/tvSubtitle"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_chainStyle="packed" />

    <TextView
        android:id="@+id/tvSubtitle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="8dp"
        android:text="@string/subtitle"
        android:textColor="@color/text_secondary"
        android:textSize="16sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/tvAppName" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginBottom="32dp"
        android:text="@string/powered_by_ai"
        android:textColor="@color/text_secondary"
        android:textSize="12sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
""",

    "app/src/main/res/layout/fragment_home.xml": """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp"
    android:background="@color/deep_navy">

    <!-- Top Bar -->
    <TextView
        android:id="@+id/tvHeader"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="LinguaX"
        android:textColor="@color/white"
        android:textSize="24sp"
        android:textStyle="bold"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <!-- Language Selector Row -->
    <LinearLayout
        android:id="@+id/langSelectorRow"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:gravity="center"
        android:layout_marginTop="24dp"
        app:layout_constraintTop_toBottomOf="@id/tvHeader">
        
        <TextView
            android:id="@+id/tvSourceLang"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"
            android:text="🇬🇧 English"
            android:textColor="@color/white"
            android:gravity="center"
            android:textSize="16sp" />

        <ImageView
            android:id="@+id/btnSwap"
            android:layout_width="40dp"
            android:layout_height="40dp"
            android:src="@android:drawable/ic_popup_sync"
            android:tint="@color/electric_blue" />

        <TextView
            android:id="@+id/tvTargetLang"
            android:layout_width="0dp"
            android:layout_weight="1"
            android:layout_height="wrap_content"
            android:text="🇮🇳 Telugu"
            android:textColor="@color/white"
            android:gravity="center"
            android:textSize="16sp" />
    </LinearLayout>

    <!-- Input Card -->
    <LinearLayout
        android:id="@+id/inputCard"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:background="@drawable/glass_card"
        android:padding="16dp"
        android:layout_marginTop="24dp"
        app:layout_constraintTop_toBottomOf="@id/langSelectorRow">

        <EditText
            android:id="@+id/etInput"
            android:layout_width="match_parent"
            android:layout_height="120dp"
            android:background="@null"
            android:gravity="top|start"
            android:hint="Type or speak text here..."
            android:textColorHint="@color/text_secondary"
            android:textColor="@color/white"
            android:textSize="18sp" />
    </LinearLayout>

    <!-- Translate Button -->
    <Button
        android:id="@+id/btnTranslate"
        android:layout_width="match_parent"
        android:layout_height="56dp"
        android:layout_marginTop="24dp"
        android:text="Translate ✦"
        android:textColor="@color/white"
        android:textSize="16sp"
        android:background="@drawable/gradient_button"
        app:backgroundTint="@null"
        app:layout_constraintTop_toBottomOf="@id/inputCard" />

    <!-- Output Card -->
    <LinearLayout
        android:id="@+id/outputCard"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:background="@drawable/glass_card"
        android:padding="16dp"
        android:layout_marginTop="24dp"
        app:layout_constraintTop_toBottomOf="@id/btnTranslate">

        <TextView
            android:id="@+id/tvOutput"
            android:layout_width="match_parent"
            android:layout_height="120dp"
            android:gravity="top|start"
            android:text="Translation will appear here..."
            android:textColor="@color/text_secondary"
            android:textSize="18sp" />
    </LinearLayout>

</androidx.constraintlayout.widget.ConstraintLayout>
""",

    "app/src/main/res/layout/fragment_history.xml": """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/deep_navy"
    android:padding="16dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Translation History"
        android:textColor="@color/white"
        android:textSize="24sp"
        android:textStyle="bold"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="No translations yet. Start translating!"
        android:textColor="@color/text_secondary"
        android:textSize="16sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>
""",

    "app/src/main/res/layout/fragment_favorites.xml": """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/deep_navy"
    android:padding="16dp">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Favorites ❤️"
        android:textColor="@color/white"
        android:textSize="24sp"
        android:textStyle="bold"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Save your favorite translations here"
        android:textColor="@color/text_secondary"
        android:textSize="16sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>
""",

    "app/src/main/res/layout/fragment_settings.xml": """<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/deep_navy"
    android:padding="16dp">

    <TextView
        android:id="@+id/tvSettingsTitle"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Settings"
        android:textColor="@color/white"
        android:textSize="24sp"
        android:textStyle="bold"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:layout_marginTop="24dp"
        app:layout_constraintTop_toBottomOf="@id/tvSettingsTitle">
        
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="APPEARANCE"
            android:textColor="@color/electric_blue"
            android:textSize="12sp"
            android:textStyle="bold" />
            
        <Switch
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Dark Mode"
            android:textColor="@color/white"
            android:checked="true"
            android:paddingTop="16dp"
            android:paddingBottom="16dp" />
            
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="DATA"
            android:layout_marginTop="16dp"
            android:textColor="@color/electric_blue"
            android:textSize="12sp"
            android:textStyle="bold" />
            
        <TextView
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="Clear History"
            android:textColor="#F44336"
            android:paddingTop="16dp"
            android:paddingBottom="16dp" />
    </LinearLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
""",

    "app/src/main/java/com/example/linguax/MainActivity.java": """package com.example.linguax;

import android.os.Bundle;
import android.view.View;
import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.NavController;
import androidx.navigation.fragment.NavHostFragment;
import androidx.navigation.ui.NavigationUI;
import com.google.android.material.bottomnavigation.BottomNavigationView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        NavHostFragment navHostFragment = (NavHostFragment) getSupportFragmentManager().findFragmentById(R.id.nav_host_fragment);
        NavController navController = navHostFragment.getNavController();
        
        BottomNavigationView bottomNav = findViewById(R.id.bottom_navigation);
        NavigationUI.setupWithNavController(bottomNav, navController);

        // Hide bottom nav on splash screen
        navController.addOnDestinationChangedListener((controller, destination, arguments) -> {
            if (destination.getId() == R.id.splashFragment) {
                bottomNav.setVisibility(View.GONE);
            } else {
                bottomNav.setVisibility(View.VISIBLE);
            }
        });
    }
}
""",

    "app/src/main/java/com/example/linguax/MockData.java": """package com.example.linguax;

import java.util.HashMap;
import java.util.Map;

public class MockData {
    public static Map<String, String> translations = new HashMap<>();
    
    static {
        translations.put("hello, how are you?", "నమస్కారం, మీరు ఎలా ఉన్నారు?");
        translations.put("hello", "నమస్కారం (Namaskaram)");
        translations.put("i love learning new languages.", "నాకు కొత్త భాషలు నేర్చుకోవడం ఇష్టం.");
        translations.put("break every language barrier", "అన్ని భాషా అడ్డంకులను బద్దలు కొట్టండి");
    }
    
    public static String getTranslation(String input) {
        String key = input.toLowerCase().trim();
        if (translations.containsKey(key)) {
            return translations.get(key);
        }
        return "అనువాదం కనుగొనబడలేదు (Translation not found for demo purposes). Try 'Hello' or 'How are you?'";
    }
}
""",

    "app/src/main/java/com/example/linguax/fragments/SplashFragment.java": """package com.example.linguax.fragments;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.navigation.Navigation;
import com.example.linguax.R;

public class SplashFragment extends Fragment {

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_splash, container, false);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        
        new Handler(Looper.getMainLooper()).postDelayed(() -> {
            Navigation.findNavController(view).navigate(R.id.action_splash_to_home);
        }, 2500);
    }
}
""",

    "app/src/main/java/com/example/linguax/fragments/HomeFragment.java": """package com.example.linguax.fragments;

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
            
            new Handler(Looper.getMainLooper()).postDelayed(() -> {
                String translated = MockData.getTranslation(textToTranslate);
                tvOutput.setText(translated);
                tvOutput.setTextColor(getResources().getColor(R.color.white, null));
                btnTranslate.setText("Translate ✦");
            }, 1000); // Fake delay for shimmer/loading effect
        });
    }
}
""",

    "app/src/main/java/com/example/linguax/fragments/HistoryFragment.java": """package com.example.linguax.fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import com.example.linguax.R;

public class HistoryFragment extends Fragment {
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_history, container, false);
    }
}
""",

    "app/src/main/java/com/example/linguax/fragments/FavoritesFragment.java": """package com.example.linguax.fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import com.example.linguax.R;

public class FavoritesFragment extends Fragment {
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_favorites, container, false);
    }
}
""",

    "app/src/main/java/com/example/linguax/fragments/SettingsFragment.java": """package com.example.linguax.fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import com.example.linguax.R;

public class SettingsFragment extends Fragment {
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_settings, container, false);
    }
}
"""
}

for path, content in files.items():
    full_path = os.path.join(project_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Project generated successfully!")

package com.example.cal;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.util.Log;


public class MainActivity extends AppCompatActivity {

    // テキストビューと計算用の変数を定義
    TextView textView;
    double result = 0;
    double num1 = 0;
    double num2 = 0;
    String operator = "";
    boolean operatorClicked = false;
    boolean eqClicked = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // テキストビューを取得
        textView = findViewById(R.id.textView);

        // 数字ボタンのクリックリスナーを設定
        Button buttonPeriod = findViewById(R.id.button_period);
        Button button0 = findViewById(R.id.button_0);
        Button button02 = findViewById(R.id.button_02);
        Button button1 = findViewById(R.id.button_1);
        Button button2 = findViewById(R.id.button_2);
        Button button3 = findViewById(R.id.button_3);
        Button button4 = findViewById(R.id.button_4);
        Button button5 = findViewById(R.id.button_5);
        Button button6 = findViewById(R.id.button_6);
        Button button7 = findViewById(R.id.button_7);
        Button button8 = findViewById(R.id.button_8);
        Button button9 = findViewById(R.id.button_9);

        // 数字ボタンのクリック処理
        View.OnClickListener numberClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(eqClicked){
                    eqClicked=false;
                    result=0;
                }
                eqClicked = false;
                if (operatorClicked) {
                    textView.setText("");
                    operatorClicked = false;
                }
                String currentText = textView.getText().toString();
                String buttonText = ((Button) view).getText().toString();
                textView.setText(currentText + buttonText);
            }
        };

        // 各数字ボタンにクリックリスナーを設定
        buttonPeriod.setOnClickListener(numberClickListener);
        button0.setOnClickListener(numberClickListener);
        button02.setOnClickListener(numberClickListener);
        button1.setOnClickListener(numberClickListener);
        button2.setOnClickListener(numberClickListener);
        button3.setOnClickListener(numberClickListener);
        button4.setOnClickListener(numberClickListener);
        button5.setOnClickListener(numberClickListener);
        button6.setOnClickListener(numberClickListener);
        button7.setOnClickListener(numberClickListener);
        button8.setOnClickListener(numberClickListener);
        button9.setOnClickListener(numberClickListener);

        // オペレーターボタンのクリックリスナーを設定
        Button buttonAdd = findViewById(R.id.button_add);
        Button buttonSub = findViewById(R.id.button_sub);
        Button buttonMulti = findViewById(R.id.button_multi);
        Button buttonDiv = findViewById(R.id.button_div);
        Button buttonEq = findViewById(R.id.button_eq);

        View.OnClickListener operatorClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!operatorClicked) {
                    operatorClicked = true;
                    eqClicked = false;
                    num1 = Double.parseDouble(textView.getText().toString());
                    operator = ((Button) view).getText().toString();
                    Log.d("MainActivity", String.valueOf(operator));
                }
            }
        };

        // オペレーターボタンにクリックリスナーを設定
        buttonAdd.setOnClickListener(operatorClickListener);
        buttonSub.setOnClickListener(operatorClickListener);
        buttonMulti.setOnClickListener(operatorClickListener);
        buttonDiv.setOnClickListener(operatorClickListener);

        // = ボタンのクリックリスナーを設定

        buttonEq.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Log.d("MainActivity", "Equal button clicked");
                if (!eqClicked){
                    eqClicked = true;
                }
                Log.d("MainActivity", String.valueOf(operatorClicked));

                Log.d("MainActivity", String.valueOf(operator));
                num2 = Double.parseDouble(textView.getText().toString());

                switch (operator) {
                    case "+":
                        result = num1 + num2;
                        Log.d("MainActivity", String.valueOf(num1));
                        Log.d("MainActivity", String.valueOf(num2));
                        break;
                    case "-":
                        result = num1 - num2;
                        break;
                    case "*":
                        result = num1 * num2;
                        break;
                    case "/":
                        if (num2 != 0) {
                            result = num1 / num2;
                        } else {
                            textView.setText("Error");
                            return;
                        }
                        break;
                }


                operatorClicked = false;
                num1=result;

                if (result == (int) result) {
                    textView.setText(String.valueOf((int) result));
                } else {
                    textView.setText(String.valueOf(result));
                }
            }
        });

        // button_c2 のクリックリスナーを設定
        Button buttonC2 = findViewById(R.id.button_c2);
        buttonC2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // result、num1、num2、operator を初期化
                result = 0;
                num1 = 0;
                num2 = 0;
                operator = "";
                textView.setText(""); // テキストビューの内容もクリア

                // その他の初期化が必要な場合はここに追加
            }
        });


    }
}

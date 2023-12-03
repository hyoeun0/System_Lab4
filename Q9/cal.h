/********************************************************************************
** Form generated from reading UI file 'Calculator.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CALCULATOR_H
#define UI_CALCULATOR_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QDialogButtonBox *buttonBox;
    QTextEdit *textEdit;
    QPushButton *btu_0;
    QPushButton *btu_1;
    QPushButton *btu_2;
    QPushButton *btu_3;
    QPushButton *btu_4;
    QPushButton *btu_5;
    QPushButton *btu_6;
    QPushButton *btu_7;
    QPushButton *btu_8;
    QPushButton *btu_9;
    QPushButton *but_plus;
    QPushButton *btu_minus;
    QPushButton *btu_multi;
    QPushButton *btu_devide;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->resize(364, 499);
        buttonBox = new QDialogButtonBox(Dialog);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setGeometry(QRect(10, 440, 341, 32));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);
        textEdit = new QTextEdit(Dialog);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        textEdit->setGeometry(QRect(40, 50, 291, 81));
        btu_0 = new QPushButton(Dialog);
        btu_0->setObjectName(QString::fromUtf8("btu_0"));
        btu_0->setGeometry(QRect(40, 280, 89, 25));
        btu_1 = new QPushButton(Dialog);
        btu_1->setObjectName(QString::fromUtf8("btu_1"));
        btu_1->setGeometry(QRect(40, 160, 89, 25));
        btu_2 = new QPushButton(Dialog);
        btu_2->setObjectName(QString::fromUtf8("btu_2"));
        btu_2->setGeometry(QRect(140, 160, 89, 25));
        btu_3 = new QPushButton(Dialog);
        btu_3->setObjectName(QString::fromUtf8("btu_3"));
        btu_3->setGeometry(QRect(240, 160, 89, 25));
        btu_4 = new QPushButton(Dialog);
        btu_4->setObjectName(QString::fromUtf8("btu_4"));
        btu_4->setGeometry(QRect(40, 200, 89, 25));
        btu_5 = new QPushButton(Dialog);
        btu_5->setObjectName(QString::fromUtf8("btu_5"));
        btu_5->setGeometry(QRect(140, 200, 89, 25));
        btu_6 = new QPushButton(Dialog);
        btu_6->setObjectName(QString::fromUtf8("btu_6"));
        btu_6->setGeometry(QRect(240, 200, 89, 25));
        btu_7 = new QPushButton(Dialog);
        btu_7->setObjectName(QString::fromUtf8("btu_7"));
        btu_7->setGeometry(QRect(40, 240, 89, 25));
        btu_8 = new QPushButton(Dialog);
        btu_8->setObjectName(QString::fromUtf8("btu_8"));
        btu_8->setGeometry(QRect(140, 240, 89, 25));
        btu_9 = new QPushButton(Dialog);
        btu_9->setObjectName(QString::fromUtf8("btu_9"));
        btu_9->setGeometry(QRect(240, 240, 89, 25));
        but_plus = new QPushButton(Dialog);
        but_plus->setObjectName(QString::fromUtf8("but_plus"));
        but_plus->setGeometry(QRect(140, 330, 89, 25));
        btu_minus = new QPushButton(Dialog);
        btu_minus->setObjectName(QString::fromUtf8("btu_minus"));
        btu_minus->setGeometry(QRect(240, 330, 89, 25));
        btu_multi = new QPushButton(Dialog);
        btu_multi->setObjectName(QString::fromUtf8("btu_multi"));
        btu_multi->setGeometry(QRect(140, 370, 89, 25));
        btu_devide = new QPushButton(Dialog);
        btu_devide->setObjectName(QString::fromUtf8("btu_devide"));
        btu_devide->setGeometry(QRect(240, 370, 89, 25));
        buttonBox->raise();
        textEdit->raise();
        btu_0->raise();
        btu_1->raise();
        btu_2->raise();
        btu_4->raise();
        btu_5->raise();
        btu_6->raise();
        btu_3->raise();
        btu_7->raise();
        btu_8->raise();
        btu_9->raise();
        but_plus->raise();
        btu_minus->raise();
        btu_multi->raise();
        btu_devide->raise();

        retranslateUi(Dialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), Dialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Dialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Calculator", nullptr));
        btu_0->setText(QApplication::translate("Dialog", "0", nullptr));
        btu_1->setText(QApplication::translate("Dialog", "1", nullptr));
        btu_2->setText(QApplication::translate("Dialog", "2", nullptr));
        btu_3->setText(QApplication::translate("Dialog", "3", nullptr));
        btu_4->setText(QApplication::translate("Dialog", "4", nullptr));
        btu_5->setText(QApplication::translate("Dialog", "5", nullptr));
        btu_6->setText(QApplication::translate("Dialog", "6", nullptr));
        btu_7->setText(QApplication::translate("Dialog", "7", nullptr));
        btu_8->setText(QApplication::translate("Dialog", "8", nullptr));
        btu_9->setText(QApplication::translate("Dialog", "9", nullptr));
        but_plus->setText(QApplication::translate("Dialog", "+", nullptr));
        btu_minus->setText(QApplication::translate("Dialog", "-", nullptr));
        btu_multi->setText(QApplication::translate("Dialog", "*", nullptr));
        btu_devide->setText(QApplication::translate("Dialog", "/", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CALCULATOR_H

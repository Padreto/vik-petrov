<?php
declare(strict_types=1);

// ── Config ────────────────────────────────────────────────────────────────────
const RECIPIENT  = 'vik-petrov@abv.bg';
const SITE_URL   = 'https://vik-petrov.com';
const SUCCESS    = SITE_URL . '/uspeshno/';
const FAIL       = SITE_URL . '/kontakti/?error=1#form';

// ── Only accept POST ──────────────────────────────────────────────────────────
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: ' . SITE_URL . '/kontakti/');
    exit;
}

// ── Honeypot — bots fill this, humans don't ───────────────────────────────────
if (!empty($_POST['bot-field'])) {
    header('Location: ' . SUCCESS); // silent discard
    exit;
}

// ── Collect & sanitize ────────────────────────────────────────────────────────
$name    = trim(htmlspecialchars(strip_tags($_POST['name']    ?? ''), ENT_QUOTES, 'UTF-8'));
$phone   = trim(htmlspecialchars(strip_tags($_POST['phone']   ?? ''), ENT_QUOTES, 'UTF-8'));
$service = trim(htmlspecialchars(strip_tags($_POST['service'] ?? ''), ENT_QUOTES, 'UTF-8'));
$message = trim(htmlspecialchars(strip_tags($_POST['message'] ?? ''), ENT_QUOTES, 'UTF-8'));

// ── Basic validation ──────────────────────────────────────────────────────────
if (empty($name) || mb_strlen($name) < 2) {
    header('Location: ' . FAIL);
    exit;
}
if (empty($phone) || !preg_match('/^[0-9\s\+\-]{6,20}$/', $phone)) {
    header('Location: ' . FAIL);
    exit;
}

// ── Build email ───────────────────────────────────────────────────────────────
$subject = '=?UTF-8?B?' . base64_encode('Нова заявка от сайта — ' . $name) . '?=';

$body  = "Нова заявка от vik-petrov.com\n";
$body .= str_repeat('─', 40) . "\n\n";
$body .= "Име:     {$name}\n";
$body .= "Телефон: {$phone}\n";
$body .= "Услуга:  " . ($service ?: 'не е избрана') . "\n";
if (!empty($message)) {
    $body .= "\nОписание:\n{$message}\n";
}
$body .= "\n" . str_repeat('─', 40) . "\n";
$body .= "Изпратено: " . date('d.m.Y H:i') . "\n";

$headers  = "From: noreply@vik-petrov.com\r\n";
$headers .= "Reply-To: noreply@vik-petrov.com\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "Content-Transfer-Encoding: 8bit\r\n";
$headers .= "X-Mailer: PHP/" . PHP_VERSION . "\r\n";

// ── Send ──────────────────────────────────────────────────────────────────────
$sent = mail(RECIPIENT, $subject, $body, $headers);

header('Location: ' . ($sent ? SUCCESS : FAIL));
exit;

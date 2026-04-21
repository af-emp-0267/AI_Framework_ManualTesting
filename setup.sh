#!/bin/bash
# ============================================================
# TMT Manual Testing Framework — One-Time Setup Script
# ============================================================
# This script copies the Knowledge Items from this repo into
# Antigravity's global knowledge directory so that the AI
# assistant loads them automatically in every conversation.
#
# Run this ONCE after cloning the repository.
# ============================================================

set -e

KNOWLEDGE_SRC="$(cd "$(dirname "$0")" && pwd)/knowledge"
KNOWLEDGE_DEST="$HOME/.gemini/antigravity/knowledge"

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║   TMT Manual Testing Framework — Setup                  ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# --- Step 1: Check source exists ---
if [ ! -d "$KNOWLEDGE_SRC" ]; then
  echo "❌  ERROR: knowledge/ folder not found in repo root."
  echo "   Make sure you are running this from the cloned repo."
  exit 1
fi

# --- Step 2: Create Antigravity knowledge directory ---
echo "📁  Creating Antigravity knowledge directory (if needed)..."
mkdir -p "$KNOWLEDGE_DEST"

# --- Step 3: Copy Knowledge Items ---
echo "📦  Copying Knowledge Items → $KNOWLEDGE_DEST/"

# Copy tmt-testing-workflow
if [ -d "$KNOWLEDGE_SRC/tmt-testing-workflow" ]; then
  mkdir -p "$KNOWLEDGE_DEST/tmt-testing-workflow/artifacts"
  cp -r "$KNOWLEDGE_SRC/tmt-testing-workflow/"* "$KNOWLEDGE_DEST/tmt-testing-workflow/"
  echo "   ✅  tmt-testing-workflow → installed"
else
  echo "   ⚠️   tmt-testing-workflow not found in repo, skipping"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅  Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Open this project folder in your IDE (VS Code, Cursor, etc.)"
echo "  2. Make sure Antigravity/Gemini extension is installed"
echo "  3. Start a new chat and the Knowledge Items will auto-load"
echo "  4. Use Skills and Workflows — see README.md for details"
echo ""
echo "Example commands you can type in chat:"
echo "  @feature-testing     → Full PRD → tested TC sheet"
echo "  @generate-tc-sheet   → Create TC sheet from PRD"
echo "  @e2e-api-testing     → Run curl-based E2E payout tests"
echo "  @quick-payout-test   → Rapid scenario testing"
echo ""
